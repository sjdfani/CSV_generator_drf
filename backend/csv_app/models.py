from pyexpat import model
from django.db import models

class File_model(models.Model):
    csv_file = models.FileField()
    
    
