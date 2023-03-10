# Generated by Django 4.1.7 on 2023-03-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("location", "0005_region_location_region_alter_state_region"),
    ]

    operations = [
        migrations.AddField(
            model_name="region",
            name="acronym",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Region Acronym"
            ),
        ),
        migrations.AlterField(
            model_name="region",
            name="name",
            field=models.TextField(
                blank=True, null=True, verbose_name="Name of the region"
            ),
        ),
    ]
