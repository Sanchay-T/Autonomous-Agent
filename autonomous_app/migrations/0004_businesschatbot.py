# Generated by Django 4.2.4 on 2023-08-20 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("autonomous_app", "0003_businesssummary"),
    ]

    operations = [
        migrations.CreateModel(
            name="BusinessChatbot",
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
                ("chatbot_key", models.CharField(max_length=1000)),
                ("chatbot_name", models.CharField(max_length=1000)),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="autonomous_app.business",
                    ),
                ),
            ],
        ),
    ]