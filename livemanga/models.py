from django.db import models
class Manga(models.Model):
    anime_name = models.CharField(max_length=200,blank=False, null=False)
    chapter_name = models.CharField(max_length=200,blank=False, null=False)
    voices_number=models.IntegerField(blank=False, null=False)
    image= models.ImageField()
    save_path = models.CharField(max_length=255,null=True)

    def __str__ (self):
        return self.name
    