from django.test import TestCase

from press.models import Redactor, Topic, Newspaper


class ModelsTests(TestCase):

    def test_redactor_str(self):
        redactor = Redactor.objects.create(
            username="test_username",
            password="test_p",
            first_name="test_first_name",
            last_name="test_last_name",
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_topic_str(self):
        topic = Topic.objects.create(
            name="test_topic"
        )
        self.assertEqual(
            str(topic),
            topic.name
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(
            name="test_topic"
        )
        newspaper = Newspaper.objects.create(
            name="test_newspaper",
            content="test_content",
            topic=topic,
        )
        self.assertEqual(
            str(newspaper),
            newspaper.name
        )
