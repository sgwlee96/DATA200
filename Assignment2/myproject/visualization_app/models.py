from django.db import models

# Create your models here.
class ProgrammingLanguageData(models.Model):
    language = models.CharField(max_length=50)
    year = models.IntegerField()
    popularity_index = models.FloatField()
    word_cloud_text = models.TextField()

    def __str__(self):
        return f"{self.language} - {self.year}"
    
    