from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)

class Item(models.Model):

    sample_1 = models.DateField(
        verbose_name='サンプル項目1 日付',
        blank=True,
        null=True,
    )

    # サンプル項目2 日付時刻
    sample_2 = models.DateTimeField(
        verbose_name='サンプル項目2 日付時刻',
        blank=True,
        null=True,
    )

    # サンプル項目3 時刻
    sample_3 = models.TimeField(
        verbose_name='サンプル項目3 日時',
        blank=True,
        null=True,
    )

    # サンプル項目4 期間 開始日
    sample_4_start = models.DateField(
        verbose_name='サンプル項目4 期間 開始日',
        blank=True,
        null=True,
    )

    # サンプル項目4 期間 終了日
    sample_4_end = models.DateField(
        verbose_name='サンプル項目4 期間 終了日',
        blank=True,
        null=True,
    )
