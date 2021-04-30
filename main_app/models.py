from django.db import models
import pandas as pd
# Create your models here.

class CSVFILE(models.Model):
    title = models.TextField(blank=True)
    file_name = models.FileField(upload_to='data_files')
    

    def __str__(self):
        return f"{self.title}"

    def delete(self, *args, **kwargs):
        self.file_name.delete()
        super().delete()