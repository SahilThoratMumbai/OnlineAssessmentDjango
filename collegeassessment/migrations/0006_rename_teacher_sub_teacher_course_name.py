# Generated by Django 5.0.3 on 2024-03-13 14:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("collegeassessment", "0005_teacher_teacher_sub"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teacher",
            old_name="teacher_sub",
            new_name="course_name",
        ),
    ]
