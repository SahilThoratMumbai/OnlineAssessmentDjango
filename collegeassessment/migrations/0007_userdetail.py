# Generated by Django 5.0.3 on 2024-03-13 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collegeassessment", "0006_rename_teacher_sub_teacher_course_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="userdetail",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=40)),
                (
                    "confirm_password",
                    models.CharField(
                        help_text="Enter above passord Correctly", max_length=40
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(help_text="Enter Phone Number", max_length=10),
                ),
                (
                    "roll_number",
                    models.CharField(
                        help_text="Enter Permanent Roll Number", max_length=20
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="collegeassessment.course",
                    ),
                ),
            ],
        ),
    ]