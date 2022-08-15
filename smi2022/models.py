from django.db import models
from django.conf import settings
from django.db.models import ForeignKey
from django.utils import timezone


# Create your models here.


# Справочник названий СМИ
class NameSmi(models.Model):
    nsmi = models.CharField(max_length=55, verbose_name="Наименование СМИ")

    def __str__(self):
        return self.nsmi

    class Meta:
        verbose_name_plural = 'Словарь Наименования СМИ'
        verbose_name = 'Наименование СМИ'
        ordering = ['id']


# Справочник СМИ

class VidSmi(models.Model):
    vsmi = models.CharField(max_length=55, verbose_name="Вид СМИ")

    def __str__(self):
        return self.vsmi

    class Meta:
        verbose_name_plural = 'Словарь Виды СМИ'
        verbose_name = 'Вид СМИ'
        ordering = ['id']


# Темы публикаций

class TemaPublik(models.Model):
    temapublik = models.CharField(max_length=85, verbose_name="Тема публикаций")

    def __str__(self):
        return self.temapublik

    class Meta:
        verbose_name_plural = 'Словарь Темы публикаций'
        verbose_name = 'Тема публикаций'
        ordering = ['id']


# Вид публикаций

class VidPublik(models.Model):
    vidpublik = models.CharField(max_length=55, verbose_name="Вид публикации")

    def __str__(self):
        return self.vidpublik

    class Meta:
        verbose_name_plural = 'Словарь Виды публикаций'
        verbose_name = 'Вид публикации'
        ordering = ['id']


# Тон публикации
class TonPublik(models.Model):
    tonpublik = models.CharField(max_length=55, verbose_name="Тон публикации")

    def __str__(self):
        return self.tonpublik

    class Meta:
        verbose_name_plural = 'Словарь Тон публикаций'
        verbose_name = 'Тон публикации'
        ordering = ['id']


# Вид рекламы
class VidReklama(models.Model):
    vidreklama = models.CharField(max_length=55, verbose_name="Вид рекламы")

    def __str__(self):
        return self.vidreklama

    class Meta:
        verbose_name_plural = 'Словарь Вид реклам'
        verbose_name = 'Вид рекламы'
        ordering = ['id']


# Вид мероприятия
class VidMeropriyatia(models.Model):
    vidmeropriyatia = models.CharField(max_length=55, verbose_name="Вид мероприятия")

    def __str__(self):
        return self.vidmeropriyatia

    class Meta:
        verbose_name_plural = 'Словарь Виды мероприятий'
        verbose_name = 'Вид мероприятия'
        ordering = ['id']


# Отделы
class Otdel(models.Model):
    otdel = models.CharField(max_length=55, verbose_name="Отдел")
    kontrol = models.IntegerField(null=True, blank=True, verbose_name="Контрольная цифра")

    def __str__(self):
        return self.otdel

    class Meta:
        verbose_name_plural = 'Словарь Отделы'
        verbose_name = 'Отдел'
        ordering = ['id']


# Публикации в СМИ
class GurnalSmi(models.Model):
    nsmi: ForeignKey = models.ForeignKey('NameSmi', null=True, on_delete=models.PROTECT,
                                         verbose_name="Название СМИ")
    vsmi: ForeignKey = models.ForeignKey('VidSmi', null=True, on_delete=models.PROTECT,
                                         verbose_name="Вид СМИ")
    name_publik = models.TextField(verbose_name="Название публикации")
    temapublik: ForeignKey = models.ForeignKey('TemaPublik', null=True, on_delete=models.PROTECT,
                                               verbose_name="Тематика публикации")
    vidpublik: ForeignKey = models.ForeignKey('VidPublik', null=True, on_delete=models.PROTECT,
                                              verbose_name="Вид публикации")
    tonpublik: ForeignKey = models.ForeignKey('TonPublik', null=True, on_delete=models.PROTECT,
                                              verbose_name="Тон публикации")
    date_publik = models.DateField(verbose_name="Дата публикации")
    url_publik = models.URLField(blank=True, verbose_name="Ссылка на публикацию")

    class Meta:
        verbose_name_plural = 'Публикации в СМИ'
        verbose_name = 'Публикация СМИ'
        ordering = ['date_publik']


# Публикации в Соц. сетях
class GurnalSocNet(models.Model):
    nsmi: ForeignKey = models.ForeignKey('NameSmi', null=True, on_delete=models.PROTECT,
                                         verbose_name="Название СМИ")
    vsmi: ForeignKey = models.ForeignKey('VidSmi', null=True, on_delete=models.PROTECT,
                                         verbose_name="Вид СМИ")
    name_publiksn = models.TextField(verbose_name="Название публикации")
    temapublik: ForeignKey = models.ForeignKey('TemaPublik', null=True, on_delete=models.PROTECT,
                                               verbose_name="Тематика публикации")
    vidpublik: ForeignKey = models.ForeignKey('VidPublik', null=True, on_delete=models.PROTECT,
                                              verbose_name="Вид публикации")
    tonpublik: ForeignKey = models.ForeignKey('TonPublik', null=True, on_delete=models.PROTECT,
                                              verbose_name="Вид публикации")
    date_publiksn = models.DateField(verbose_name="Дата публикации")
    url_publiksn = models.URLField(verbose_name="Ссылка на публикацию")

    class Meta:
        verbose_name_plural = 'Публикации в Соц. сетях'
        verbose_name = 'Публикация в Соц. сетях'
        ordering = ['date_publiksn']


# Пресс-релизы
class PressRelease(models.Model):
    name_press = models.TextField(null=True, blank=True,
                                  verbose_name="Название пресс-релиза")
    temapublik: ForeignKey = models.ForeignKey('TemaPublik', null=True, on_delete=models.PROTECT,
                                               verbose_name="Тематика публикации")
    date_press = models.DateField(verbose_name="Дата пресс-релиза")

    class Meta:
        verbose_name_plural = 'Пресс-релизы'
        verbose_name = 'Пресс-релиз'
        ordering = ['date_press']


# Реклама СМИ
class ReklamaSmi(models.Model):
    vidreklama: ForeignKey = models.ForeignKey('VidReklama', null=True, on_delete=models.PROTECT,
                                               verbose_name="Вид рекламы")
    temapublik: ForeignKey = models.ForeignKey('TemaPublik', null=True, on_delete=models.PROTECT,
                                               verbose_name="Тематика публикации")
    date_reklama = models.DateField(verbose_name="Дата рекламы")
    kolvareklama = models.IntegerField(null=True, blank=True, verbose_name="Кол-во рекламы")

    class Meta:
        verbose_name_plural = 'Реклама в СМИ'
        verbose_name = 'Реклама СМИ'
        ordering = ['date_reklama']


# Мероприятия СМИ по отделам
class SmiOtdels(models.Model):
    vidmeropriyatia: ForeignKey = models.ForeignKey('VidMeropriyatia', null=True, on_delete=models.PROTECT,
                                                    verbose_name="Вид мероприятия")
    temapublik: ForeignKey = models.ForeignKey('TemaPublik', null=True, on_delete=models.PROTECT,
                                               verbose_name="Тематика публикации")
    otdel: ForeignKey = models.ForeignKey('Otdel', null=True, on_delete=models.PROTECT,
                                          verbose_name="Отдел")
    date_smiotdel = models.DateField(verbose_name="Дата мероприятия")

    class Meta:
        verbose_name_plural = 'Мероприятия СМИ по отделам'
        verbose_name = 'Мероприятие СМИ'
        ordering = ['date_smiotdel']
