from django.db import models


class Account(models.Model):
    """ Account class """

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        ordering = ('date', "number",)

    number = models.CharField(max_length=15, verbose_name="Номер счета")
    date = models.DateField(verbose_name="Дата счета", null=True, blank=True)
    paid = models.BooleanField(verbose_name="Оплачено", default=False)

    def __str__(self):
        return f"Счет №{self.number} от {self.date}"


class Device(models.Model):
    """ Device type """

    class Meta:
        verbose_name = "Тип прибора"
        verbose_name_plural = "Типы приборов"

    name = models.CharField(max_length=20, verbose_name="Тип устройства")

    def __str__(self):
        return f"{self.name}"


class Complaint(models.Model):
    """ Complaint class """

    class Meta:
        verbose_name = "Рекламация"
        verbose_name_plural = "Рекламации"
        ordering = ("date", "number",)

    STATUS_CHOICES = (
        ("new", 'Новая рекламация'),
        ("work", 'В работе'),
        ("done", 'Закрыта'),
    )

    number = models.CharField(max_length=15, verbose_name="Номер рекламации")
    date = models.DateField(verbose_name="Дата рекламации")
    completed_date = models.DateField(verbose_name="Дата закрытия рекламации", null=True, blank=True)
    date_at_work = models.DateField(verbose_name="Дата выезда", null=True, blank=True)
    files_attached = models.BooleanField(verbose_name="Файлы к рекламации", default=False)
    status = models.CharField(verbose_name='Статус', max_length=5, choices=STATUS_CHOICES, default="new")
    description = models.CharField(max_length=2048, verbose_name="Описание клиента", null=True, blank=True)
    address_main = models.CharField(max_length=1024, verbose_name="Адрес рекламации", null=True, blank=True)
    address_additional = models.CharField(max_length=50, verbose_name="Адрес (подъезд, этаж)", null=True, blank=True)
    client_name = models.CharField(max_length=150, verbose_name="Имя клиента", null=True, blank=True)
    client_phone = models.CharField(max_length=20, verbose_name="Телефон клиента", null=True, blank=True)
    client_email = models.CharField(max_length=100, verbose_name="Email клиента", null=True, blank=True)
    device_type = models.ForeignKey(Device, verbose_name="Тип устройства", on_delete=models.SET_NULL, null=True,
                                    blank=True)
    additional_comment = models.CharField(max_length=2048, verbose_name="Комментарий",
                                          help_text="Доп. инфо, зайти после 14.00", null=True, blank=True)
    print_order = models.IntegerField(verbose_name="Сортировка при печати", default=0)
    price = models.IntegerField(verbose_name="Стоимость заявки", null=True, blank=True)
    transport_hours = models.IntegerField(verbose_name="Количество часов дороги", null=True, blank=True)
    act_photo = models.ImageField(verbose_name="Фото акта", upload_to='acts/%Y/%m', null=True, blank=True)

    account = models.ForeignKey(Account, verbose_name="Счет", on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="complaints")

    def __str__(self):
        return f"Рекламация №{self.number} от {self.date}"
