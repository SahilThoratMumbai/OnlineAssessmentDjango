# Generated by Django 5.0.3 on 2024-03-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collegeassessment", "0010_assignment_subject"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=30)),
                ("description", models.TextField(max_length=350)),
            ],
        ),
    ]
