from django.db import models

# Create your models here.


class Parking(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description


class Zone(models.Model):
    zone_id = models.CharField(max_length=1)
    description = models.CharField(max_length=30)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.zone_id, self.description)


class Place(models.Model):
    is_free = models.BooleanField(default=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.is_free, self.zone.zone_id)
