from django.db import models


class Parking(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description


class Zone(models.Model):
    zone_id = models.CharField(max_length=1)
    description = models.CharField(max_length=30)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Place(models.Model):
    number = models.IntegerField(default=1)
    is_taken = models.BooleanField(default=False)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.number
