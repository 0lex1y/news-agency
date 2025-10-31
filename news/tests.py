from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from .models import Topics, Newspaper, Redactor


class TopicsModelTest(TestCase):
    def setUp(self):
        self.topic = Topics.objects.create(name="War")

    def test_topic_str(self):
        self.assertEqual(
            str(self.topic), "War"
        )  # перевірка чи правильно створюється назва теми


class NewspaperModelTest(TestCase):
    def setUp(self):
        self.topic = Topics.objects.create(name="War")
        self.publisher = Redactor.objects.create_user(
            username="Tomkin",
            password="testpassword123",
            years_of_experience=5
        )
        self.newspaper = Newspaper.objects.create(
            title="War in Ukraine",
            topic=self.topic,
            content="The War is in Ukraine start in 2022",
        )
        self.newspaper.publisher.add(self.publisher)

    def test_newspaper_str(self):
        self.assertEqual(str(self.newspaper.title), "War in Ukraine")

    def test_newspaper_has_publisher(self):
        self.assertIn(self.publisher, self.newspaper.publisher.all())


class RedactorModelTest(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username="Tomkin",
            password="testpassword123",
            years_of_experience=5
        )

    def test_redactor_str(self):
        self.assertEqual(str(self.redactor.username), "Tomkin")

    def test_redactor_years_of_experience(self):
        self.assertEqual(self.redactor.years_of_experience, 5)

    def test_redactor_username_unique(self):
        with self.assertRaises(IntegrityError):
            Redactor.objects.create_user(
                username="Tomkin",
                password="testpassword123",
                years_of_experience=5
            )


class NewspaperListViewTest(TestCase):
    def setUp(self):
        self.topic = Topics.objects.create(name="War")
        self.topic2 = Topics.objects.create(name="Peace")
        self.newspaper = Newspaper.objects.create(
            title="War in Ukraine",
            content="The War is in Ukraine start in 2022",
            topic=self.topic,
        )
        self.newspaper2 = Newspaper.objects.create(
            title="Peace in Ukraine",
            content="The War is in Ukraine end in 2025",
            topic=self.topic2,
        )

    def test_newspaper_status_code(self):
        response = self.client.get(reverse("news:index"))
        self.assertEqual(response.status_code, 200)

    def test_newspaper_template(self):
        response = self.client.get(reverse("news:index"))
        self.assertTemplateUsed(response, "news/index.html")

    def test_newspaper_context(self):
        response = self.client.get(reverse("news:index"))
        newspapers = response.context["newspapers"]
        self.assertEqual(len(newspapers), 2)
        self.assertIn(self.newspaper, newspapers)
        self.assertIn(self.newspaper2, newspapers)


class NewspaperDetailViewTest(TestCase):
    def setUp(self):
        self.topic = Topics.objects.create(name="War")
        self.newspaper = Newspaper.objects.create(
            title="War in Ukraine",
            topic=self.topic,
            content="The War is in Ukraine start in 2022",
        )
        self.publisher = Redactor.objects.create_user(
            username="Tomkin",
            password="testpassword123",
            years_of_experience=5
        )
        self.newspaper.publisher.add(self.publisher)

    def test_newspaper_status_code(self):
        response = self.client.get(
            reverse("news:news_detail", args=[self.newspaper.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_newspaper_template(self):
        response = self.client.get(
            reverse("news:news_detail", args=[self.newspaper.id])
        )
        self.assertTemplateUsed(response, "news/newspaper_detail.html")

    def test_newspaper_context(self):
        response = self.client.get(
            reverse("news:news_detail", args=[self.newspaper.id])
        )
        newspaper = response.context["newspaper"]
        self.assertEqual(newspaper, self.newspaper)
        self.assertEqual(newspaper.title, "War in Ukraine")
        self.assertEqual(newspaper.topic, self.topic)
        self.assertEqual(
            newspaper.content,
            "The War is in Ukraine start in 2022")


class RedactorsCreteFormTest(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username="Tomkin",
            password="testpassword123",
            years_of_experience=5
        )

    def test_redactor_create_status_code(self):
        response = self.client.get(reverse("news:redactors_create"))
        self.assertEqual(response.status_code, 200)

    def test_redactor_create_form(self):
        response = self.client.get(reverse("news:redactors_create"))
        self.assertTemplateUsed(response, "news/redactor_form.html")

    def test_redactor_create(self):
        data = {
            "username": "Tomkin",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "years_of_experience": 5,
        }
        response = self.client.post(reverse("news:redactors_create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Redactor.objects.count(), 1)
        redactor = Redactor.objects.first()
        self.assertEqual(redactor.username, "Tomkin")
        self.assertEqual(redactor.years_of_experience, 5)
