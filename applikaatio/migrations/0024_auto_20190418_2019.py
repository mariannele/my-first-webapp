# Generated by Django 2.1.5 on 2019-04-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applikaatio', '0023_auto_20190418_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstrip',
            name='city_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
