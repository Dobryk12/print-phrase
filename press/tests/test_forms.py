from django.contrib.auth import get_user_model
from django.test import TestCase
from press.forms import (
    NewspaperForm,
    NewspaperSearchForm,
    RedactorFormForLogin,
    RedactorFormForUpdate,
    RedactorSearchForm,
    TopicForm,
    TopicSearchForm,
)


class TestForms(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user",
            password="password123",
        )

    # def test_newspaper_form(self):
    #     form_data = {
    #         "name": "Test Newspaper",
    #         "content": "Test Content",
    #         "topic": "Sports",
    #     }
    #     form = NewspaperForm(data=form_data)
    #     self.assertTrue(form.is_valid())

    def test_newspaper_search_form(self):
        form = NewspaperSearchForm(data={"name": "Test"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Test")

    # def test_redactor_form_for_login(self):
    #     form_data = {
    #         "username": "test_user",
    #         "password1": "password123",
    #         "password2": "password123",
    #         "first_name": "Stan",
    #         "last_name": "Shady",
    #         "years_of_experience": "5",
    #     }
    #     form = RedactorFormForLogin(data=form_data)
    #     self.assertTrue(form.is_valid())

    def test_redactor_form_for_update(self):
        form_data = {
            "username": "test_user",
            "first_name": "Stan",
            "last_name": "Shady",
            "years_of_experience": "5",
            "email": "test@example.com",
            "password": "password123",
        }
        form = RedactorFormForUpdate(data=form_data)
        self.assertTrue(form.is_valid())

    def test_redactor_search_form(self):
        form = RedactorSearchForm(data={"username": "Test"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "Test")

    def test_topic_form(self):
        form_data = {
            "name": "Test Topic",
            "description": "Test Description",
        }
        form = TopicForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_topic_search_form(self):
        form = TopicSearchForm(data={"name": "Test"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Test")
