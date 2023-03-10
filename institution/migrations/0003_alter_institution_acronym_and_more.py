# Generated by Django 4.1.7 on 2023-02-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("institution", "0002_alter_institution_creator_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="acronym",
            field=models.TextField(
                blank=True, null=True, verbose_name="Institution Acronym"
            ),
        ),
        migrations.AlterField(
            model_name="institution",
            name="institution_type",
            field=models.TextField(
                blank=True,
                choices=[
                    ("", ""),
                    ("agência de apoio à pesquisa", "agência de apoio à pesquisa"),
                    (
                        "universidade e instâncias ligadas à universidades",
                        "universidade e instâncias ligadas à universidades",
                    ),
                    (
                        "empresa ou instituto ligadas ao governo",
                        "empresa ou instituto ligadas ao governo",
                    ),
                    ("organização privada", "organização privada"),
                    (
                        "organização sem fins de lucros",
                        "organização sem fins de lucros",
                    ),
                    (
                        "sociedade científica, associação pós-graduação, associação profissional",
                        "sociedade científica, associação pós-graduação, associação profissional",
                    ),
                    ("outros", "outros"),
                ],
                null=True,
                verbose_name="Institution Type",
            ),
        ),
        migrations.AlterField(
            model_name="institution",
            name="level_1",
            field=models.TextField(
                blank=True, null=True, verbose_name="Organization Level 1"
            ),
        ),
        migrations.AlterField(
            model_name="institution",
            name="level_2",
            field=models.TextField(
                blank=True, null=True, verbose_name="Organization Level 2"
            ),
        ),
        migrations.AlterField(
            model_name="institution",
            name="level_3",
            field=models.TextField(
                blank=True, null=True, verbose_name="Organization Level 3"
            ),
        ),
        migrations.AlterField(
            model_name="institution",
            name="name",
            field=models.TextField(blank=True, null=True, verbose_name="Nome"),
        ),
    ]
