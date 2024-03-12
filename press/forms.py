from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


from press.models import Redactor, Newspaper, Topic


class NewspaperForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    topic = forms.ModelChoiceField(queryset=Topic.objects.all())
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class RedactorFormForLogin(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience"
        )
        widgets = {
            "years_of_experience": forms.NumberInput(
                attrs={
                    "placeholder": "Enter your years of experience",
                    "class": "form-control"
                }
            )
        }


class RedactorFormForUpdate(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = [
            "username",
            "first_name",
            "last_name",
            "years_of_experience",
            "email",
            "password"
        ]


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class TopicForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Topic
        fields = "__all__"


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )
