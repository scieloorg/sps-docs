# Generated by Django 4.1.7 on 2023-04-06 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("spstaglib", "0002_alter_example_title_alter_example_xml_code_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="SPSAttribute",
            fields=[
                (
                    "spsbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="spstaglib.spsbase",
                    ),
                ),
            ],
            options={
                "verbose_name": "Attribute",
                "verbose_name_plural": "Attributes",
            },
            bases=("spstaglib.spsbase",),
        ),
    ]
