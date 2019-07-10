from django.db import models

# Create your models here.


class Image(models.Model):
    title = models.TextField()
    cover = models.ImageField(blank=True,null=True, upload_to='images/')

    def __str__(self):
        return self.title
