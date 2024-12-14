# Generated by Django 5.1.4 on 2024-12-14 07:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_cover",
                    models.ImageField(
                        upload_to="blog_images", verbose_name="Обложка изображения"
                    ),
                ),
                (
                    "date",
                    models.DateField(auto_now_add=True, verbose_name="Дата публикации"),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Заголовок статьи"),
                ),
                (
                    "page_slug",
                    models.SlugField(unique=True, verbose_name="Слаг страницы"),
                ),
                (
                    "main_title",
                    models.CharField(max_length=200, verbose_name="Основной заголовок"),
                ),
                ("text_first", ckeditor.fields.RichTextField(verbose_name="Текст 1")),
                ("text_second", ckeditor.fields.RichTextField(verbose_name="Текст 2")),
                (
                    "image_first",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog_images",
                        verbose_name="Первое изображение",
                    ),
                ),
                (
                    "image_second",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog_images",
                        verbose_name="Второе изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Блог",
                "verbose_name_plural": "Блог",
            },
        ),
        migrations.CreateModel(
            name="Faq",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300, verbose_name="Титул")),
                ("text", models.TextField(verbose_name="Текст")),
                ("page_slug", models.SlugField(verbose_name="Слаг страницы")),
            ],
            options={
                "verbose_name": "Часто задаваемые вопросы",
                "verbose_name_plural": "Часто задаваемые вопросы",
            },
        ),
        migrations.CreateModel(
            name="OurTeam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Имя")),
                (
                    "image",
                    models.ImageField(
                        upload_to="OurTeam_images", verbose_name="изображение"
                    ),
                ),
                ("job", models.CharField(max_length=200, verbose_name="Работа")),
                ("description", models.TextField(verbose_name="описание")),
            ],
            options={
                "verbose_name": "Наша команда",
                "verbose_name_plural": "Наша команда",
            },
        ),
        migrations.CreateModel(
            name="Rezident",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Имя")),
                (
                    "image",
                    models.ImageField(
                        upload_to="rezident_images", verbose_name="изображение"
                    ),
                ),
                ("job", models.CharField(max_length=200, verbose_name="Работа")),
                ("description", models.TextField(verbose_name="описание")),
            ],
            options={
                "verbose_name": "Резидент",
                "verbose_name_plural": "Резидент",
            },
        ),
        migrations.CreateModel(
            name="Space",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("space", models.CharField(max_length=300, verbose_name="места")),
                (
                    "page_slug",
                    models.SlugField(unique=True, verbose_name="Слаг страницы"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="Images/space", verbose_name="изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "места",
                "verbose_name_plural": "места",
            },
        ),
    ]
