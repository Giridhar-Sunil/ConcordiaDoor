# Generated by Django 4.2.19 on 2025-03-03 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listtextbook", "0002_rename_availabilty_textbook_availability"),
    ]

    operations = [
        migrations.AddField(
            model_name="textbook",
            name="condition",
            field=models.CharField(
                choices=[("new", "New"), ("written", "Written"), ("old", "Old")],
                default="new",
                max_length=10,
            ),
        ),
    ]
