# Generated by Django 2.1.5 on 2019-04-18 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applikaatio', '0024_auto_20190418_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstrip',
            name='content',
            field=models.TextField(default=None),
        ),
    ]
