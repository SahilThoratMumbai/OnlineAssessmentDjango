# Generated by Django 5.0.3 on 2024-03-13 11:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("collegeassessment", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="assignment",
            name="course",
        ),
        migrations.RemoveField(
            model_name="subject",
            name="course_name",
        ),
        migrations.DeleteModel(
            name="Teacher",
        ),
        migrations.RemoveField(
            model_name="userdetail",
            name="branch",
        ),
        migrations.DeleteModel(
            name="Assignment",
        ),
        migrations.DeleteModel(
            name="subject",
        ),
        migrations.DeleteModel(
            name="userdetail",
        ),
    ]
