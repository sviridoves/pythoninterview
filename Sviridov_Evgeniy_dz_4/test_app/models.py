from django.db import models


class Good_Item(models.Model):
    title = models.CharField(
        verbose_name=u'Название',
        max_length=255
    )

    receipted_date = models.DateTimeField(
        verbose_name=u'Дата поступления',
        auto_created=True,
        auto_now_add=True
    )

    price = models.PositiveIntegerField(
        verbose_name=u'Цена',
        default=0
    )

    measure = models.CharField(
        verbose_name=u'Единица измерения',
        max_length=20
    )

    vendor = models.CharField(
        verbose_name=u'Поставщик',
        max_length=255
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Карточка товара'
        verbose_name_plural = u'Карточки товаров'
