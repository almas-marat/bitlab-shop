from django.db import models

class Films(models.Model):
    name = models.CharField("Название фильма", max_length=30)
    mainactor = models.CharField("Главный актер фильма", max_length=50)
    year = models.IntegerField("Год выпуска фильма", default=2000)

    class Meta:
        verbose_name_plural = 'Films'

    def __init__(self):
        return self.name

