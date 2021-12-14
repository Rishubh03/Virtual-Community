from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=200, unique=True)
    textarea = models.TextField()
    image = models.ImageField(upload_to='wiki/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Articles"
