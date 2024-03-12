from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from press.models import Newspaper, Redactor, Topic


class TestLoginRequired(TestCase):

    def setUp(self):
        self.client = Client()
        self.redactor = get_user_model().objects.create_user(
            username="testuser", email="test@example.com", password="secret"
        )

    def test_login_required_for_newspaper_list(self):
        response = self.client.get(reverse("press:newspaper-list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/newspapers/")

    def test_login_required_for_redactor_list(self):
        response = self.client.get(reverse("press:redactor-list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/redactors/")

    def test_login_required_for_topic_list(self):
        response = self.client.get(reverse("press:topic-list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/topics/")

    def test_login_required_for_newspaper_create(self):
        response = self.client.get(reverse("press:newspaper-create"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/newspapers/create")

    def test_login_required_for_topic_create(self):
        response = self.client.get(reverse("press:topic-create"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/topics/create/")

    def test_login_required_for_newspaper_update(self):
        topic = Topic.objects.create(name="Test Topic")
        newspaper = Newspaper.objects.create(name="Test Newspaper", content="Test Content", topic=topic)
        response = self.client.get(reverse("press:newspaper-update", kwargs={"pk": newspaper.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/newspapers/{newspaper.pk}/update")

    def test_login_required_for_redactor_update(self):
        redactor = Redactor.objects.create(username="test_redactor")
        response = self.client.get(reverse("press:redactor-update", kwargs={"pk": redactor.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/redactors/{redactor.pk}/update/")

    def test_login_required_for_topic_update(self):
        topic = Topic.objects.create(name="Test Topic")
        response = self.client.get(reverse("press:topic-update", kwargs={"pk": topic.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/topics/{topic.pk}/update/")

    def test_login_required_for_newspaper_delete(self):
        topic = Topic.objects.create(name="Test Topic")
        newspaper = Newspaper.objects.create(name="Test Newspaper", content="Test Content", topic=topic)
        response = self.client.get(reverse("press:newspaper-delete", kwargs={"pk": newspaper.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/newspapers/{newspaper.pk}/delete/")

    def test_login_required_for_redactor_delete(self):
        redactor = Redactor.objects.create(username="test_redactor")
        response = self.client.get(reverse("press:redactor-delete", kwargs={"pk": redactor.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/redactors/{redactor.pk}/delete/")

    def test_login_required_for_topic_delete(self):
        topic = Topic.objects.create(name="Test Topic")
        response = self.client.get(reverse("press:topic-delete", kwargs={"pk": topic.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/topics/{topic.pk}/delete/")
