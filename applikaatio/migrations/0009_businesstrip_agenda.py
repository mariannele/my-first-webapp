# Generated by Django 2.1.5 on 2019-04-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applikaatio', '0008_auto_20190404_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstrip',
            name='agenda',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
