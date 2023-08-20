# Generated by Django 4.2.4 on 2023-08-20 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("autonomous_app", "0002_businesschathistory"),
    ]

    operations = [
        migrations.CreateModel(
            name="BusinessSummary",
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
                ("summary", models.TextField(max_length=100000)),
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