# Generated by Django 4.2.7 on 2023-11-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comm", "0002_blogpost_cover_alter_blogpost_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
