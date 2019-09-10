from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_delete
from django.dispatch import receiver
# Create your models here.


class Excursion(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField('Название экскурсии',max_length=100)
    ticket_qty=models.IntegerField('Количество билетов')
    ticket_price=models.IntegerField('Стоимость обычного билета')
    discount_ticket_price=models.IntegerField('Стоимость льготного билета')
    time=models.TimeField('Время экскурсии')

    class Meta:
        verbose_name = "Экскурсия"
        verbose_name_plural = "Экскурсии"


    def __str__(self):
        return self.name

class Tickets(models.Model):
    date=models.DateField(auto_now = True)
    excurs=models.ForeignKey('Excursion',on_delete=models.CASCADE,verbose_name='Экскурсия')
    normal_ticket=models.PositiveIntegerField('Количество обычных билетов')
    discount_ticket = models.PositiveIntegerField('Количество льготных билетов')
    free_ticket=models.PositiveIntegerField('Количество бесплатных билетов')
    cashier=models.CharField('ФИ Кассира',max_length=100)

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"

    def __str__(self):
        return "Билет: количество("+ str(self.normal_ticket+self.free_ticket)+")"

    def save(self, *args, **kwargs):
        moss=Excursion.objects.get(name=self.excurs)
        moss.ticket_qty -= self.normal_ticket
        moss.ticket_qty -= self.discount_ticket
        moss.ticket_qty -= self.free_ticket
        moss.save()
        super(Tickets, self).save(*args, **kwargs)





