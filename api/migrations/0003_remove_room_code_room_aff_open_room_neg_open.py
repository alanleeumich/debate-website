# Generated by Django 4.1.1 on 2022-09-12 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_remove_room_topic_room_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="code",
        ),
        migrations.AddField(
            model_name="room",
            name="aff_open",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="room",
            name="neg_open",
            field=models.BooleanField(default=True),
        ),
    ]