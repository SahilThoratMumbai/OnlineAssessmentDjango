# Generated by Django 5.0.3 on 2024-03-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collegeassessment", "0012_rename_news_new"),
    ]

    operations = [
        migrations.CreateModel(
            name="Upload",
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
                ("ass_desc", models.CharField(max_length=200)),
                (
                    "upload_ass",
                    models.FileField(blank=True, null=True, upload_to="uploads/"),
                ),
            ],
        ),
    ]
