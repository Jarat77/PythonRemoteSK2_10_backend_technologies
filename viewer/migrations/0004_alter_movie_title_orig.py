# Generated by Django 4.1.1 on 2023-01-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_agerestriction_award_awardcategory_country_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title_orig',
            field=models.CharField(max_length=64),
        ),
    ]
