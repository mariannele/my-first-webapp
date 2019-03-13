# Generated by Django 2.1.5 on 2019-03-13 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Businesstrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('travel_date', models.DateField(default=django.utils.timezone.now)),
                ('total_km', models.IntegerField()),
                ('notes', models.TextField()),
            ],
        ),
    ]
