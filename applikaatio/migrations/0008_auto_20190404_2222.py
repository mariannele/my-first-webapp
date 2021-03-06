# Generated by Django 2.1.5 on 2019-04-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applikaatio', '0007_auto_20190404_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstrip',
            name='return_trip',
            field=models.CharField(choices=[('ONE_WAY', 'One way'), ('RETURN', 'Return trip')], default='RETURN', max_length=3),
        ),
        migrations.AlterField(
            model_name='businesstrip',
            name='reason',
            field=models.CharField(choices=[('CUSTOMER_MEETING', 'Customer meeting'), ('SUPPLIER_MEETING', 'Supplier meeting'), ('OTHER_MEETING', 'Other meeting'), ('INTERNAL_MEETING', 'Internal meeting'), ('OFFICE_DAY', 'Office day'), ('TRADE_FAIR', 'Trade fair')], default='CUSTOMER_MEETING', max_length=2),
        ),
    ]
