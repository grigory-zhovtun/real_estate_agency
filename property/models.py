from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



class Owner(models.Model):
    name = models.CharField('ФИО собственника', max_length=200)
    phone = models.CharField('Номер телефона', max_length=20)
    pure_phone = PhoneNumberField(
        'Нормализованный номер телефона',
        blank=True
    )
    owned_flats = models.ManyToManyField(
        'Flat',
        related_name='property_owners',
        blank=True,
        verbose_name='Квартиры в собственности'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Собственник'
        verbose_name_plural = 'Собственники'



class Flat(models.Model):
    owners = models.ManyToManyField(
        Owner,
        related_name="flats",
        blank=True,
        verbose_name='Квартиры в собственности'
    )

    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)

    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', null=True, blank=True, db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField(
        'Новостройка',
        null=True,
        blank=True,
        db_index=True,
    )
    liked_by = models.ManyToManyField(
        User,
        related_name="liked_posts",
        blank=True,
        verbose_name="Кто лайкнул"
    )
    owner_pure_phone = PhoneNumberField(
        'Нормализованный номер владельца',
        blank=True,
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='complaints',
        verbose_name='Пользователь',
        help_text='Пользователь, подавший жалобу'
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        related_name='complaints',
        verbose_name='Квартира',
        help_text='Квартира, на которую пожаловались:'
    )
    text = models.TextField(
        "Текст жалобы:"
    )
    created_at = models.DateTimeField(
        "Когда создана жалоба",
        default=timezone.now,
        db_index=True
    )

    def __str__(self):
        return f'Жалоба от {self.user.username} на {self.flat}'