# Generated by Django 2.1.7 on 2019-09-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilets', '0013_tickets_ticket_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='discount_ticket_price',
            field=models.PositiveIntegerField(verbose_name='Стоимость льготного билета'),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='ticket_price',
            field=models.PositiveIntegerField(verbose_name='Стоимость обычного билета'),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='ticket_qty',
            field=models.PositiveIntegerField(verbose_name='Количество билетов'),
        ),
    ]
