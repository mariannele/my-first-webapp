# Generated by Django 2.1.5 on 2019-04-19 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applikaatio', '0025_auto_20190418_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesstrip',
            options={'ordering': ('-travel_date',)},
        ),
    ]
