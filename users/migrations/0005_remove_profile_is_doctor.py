# Generated by Django 4.1.2 on 2022-10-09 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_profile_is_doctor"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="is_doctor",),
    ]