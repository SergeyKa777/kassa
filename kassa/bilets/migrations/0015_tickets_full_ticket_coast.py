# Generated by Django 2.1.7 on 2019-09-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilets', '0014_auto_20190910_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='full_ticket_coast',
            field=models.PositiveIntegerField(default=1, verbose_name='Полная стоимость всех билетов'),
            preserve_default=False,
        ),
    ]
