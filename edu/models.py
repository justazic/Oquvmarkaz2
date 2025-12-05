from django.db import models

# Create your models here.

class Yonalish(models.Model):
    nomi = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nomi
    
    
class OquvMarkaz(models.Model):
    yonalish = models.ForeignKey(Yonalish,on_delete=models.CASCADE)
    markaz_nomi = models.CharField(max_length=200)
    kurs_nomi = models.CharField(max_length=200)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    malumot = models.TextField()
    rasm = models.ImageField(upload_to='markazlar/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.markaz_nomi} - {self.kurs_nomi}"
    