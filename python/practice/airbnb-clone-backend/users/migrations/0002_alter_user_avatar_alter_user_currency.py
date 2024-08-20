# Generated by Django 4.2.15 on 2024-08-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="user",
            name="currency",
            field=models.CharField(
                choices=[("krw", "Korean won"), ("usd", "Us dollar")], max_length=5
            ),
        ),
    ]
