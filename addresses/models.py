from django.db import models


class Building(models.Model):
    id = models.IntegerField(primary_key=True)
    prefix_id = models.IntegerField(blank=True, null=True)
    district_id = models.IntegerField(blank=True, null=True)
    house = models.TextField(blank=True, null=True)
    corpus = models.TextField(blank=True, null=True)
    liter = models.TextField(blank=True, null=True)
    villa = models.TextField(blank=True, null=True)
    parcel = models.TextField(blank=True, null=True)
    full_address = models.TextField(blank=True, null=True)
    is_updated = models.BooleanField(blank=True, null=True)
    is_actual = models.BooleanField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    municipality_id = models.FloatField(blank=True, null=True)
    short_address = models.TextField(blank=True, null=True)
    post_prefix = models.TextField(blank=True, null=True)
    build_number = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buildings'
