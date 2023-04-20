from django.db import models

# Create your models here.
from django.db import models

class Yeardata(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_49_avg_digital_inclusion_index = models.FloatField(db_column='14-49_Avg_Digital_Inclusion_Index', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_50_avg_digital_inclusion_index = models.FloatField(db_column='50+_Avg_Digital_Inclusion_Index', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_49_avg_digital_accessibility_index = models.FloatField(db_column='14-49_Avg_Digital_Accessibility_Index', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_50_avg_digital_accessibility_index = models.FloatField(db_column='50+_Avg_Digital_Accessibility_Index', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_49_avg_digital_ability_index = models.FloatField(db_column='14-49_Avg_Digital_Ability_Index', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_50_avg_digital_ability_index = models.FloatField(db_column='50+_Avg_Digital_Ability_Index', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yearData'