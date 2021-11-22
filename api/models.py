from django.db import models

# Create your models here.


class FastTextModel(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    file = models.FileField()

    def __str__(self):
        return str(self.file)[:-4]


class DataForTrain(models.Model):
    file = models.FileField()


class DownloadModel(models.Model):
    file = models.FileField()