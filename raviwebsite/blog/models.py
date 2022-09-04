from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    copyright = models.CharField(max_length=300)

    class Meta:
        db_table = "banner"
        verbose_name = "banner"
        verbose_name_plural = "banner"