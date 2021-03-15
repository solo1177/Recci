from django.db import models

# Create your models here.
class User(models.Model):
    """ユーザーのモデル"""
    name = models.CharField(max_length=256)
    count = models.IntegerField(default=1)
    date = models.DateField()
    memo = models.TextField(default="")
    user = models.CharField(max_length=256)
    
    def __str__(self):
        return '<User:id=' + str(self.id) +','+ self.name + '('+ str(self.count) +')>'

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='image', default='defo')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '<Documents:id=' + str(self.id) +',>'

class Recipe(models.Model):
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    time = models.CharField(max_length=256)
    cost = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    def __str__(self):
        return '<Reccip:id=' + str(self.id) +',>'
