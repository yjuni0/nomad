# Generated by Django 4.2.15 on 2024-08-13 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_room_name_alter_amenity_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Amenities"},
        ),
    ]
