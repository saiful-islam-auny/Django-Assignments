# Generated by Django 5.0.2 on 2024-06-29 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                (
                    "borrowing_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="library/media/uploads/"
                    ),
                ),
                ("borrow_book", models.BooleanField(default=False)),
                ("category", models.ManyToManyField(to="category.category")),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("body", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="library.book",
                    ),
                ),
            ],
        ),
    ]
