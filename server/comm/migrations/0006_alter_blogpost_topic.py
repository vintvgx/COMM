# Generated by Django 4.2.7 on 2023-12-02 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("comm", "0005_topic_blogpost_topic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="topic",
            field=models.ForeignKey(
                default="Other",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="topics",
                to="comm.topic",
            ),
        ),
    ]
