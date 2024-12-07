from django.db import models

class Category (models.Model):
    name = models.CharField(max_length=100,verbose_name='Categoriya ismini kiriting',unique=True)

    def __str__(self):
        return self.name

class Book (models.Model):
    title = models.CharField(max_length=200,verbose_name='Kitob nomi')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='categoriya')
    publication_date = models.DateField(auto_now_add=True,verbose_name='Nashir sanasi')
    isbn = models.CharField(max_length=13,unique=True,verbose_name= "Kitobning ISBN raqami")
    genre = models.CharField(max_length=100,verbose_name="Kitob janri")
    summary = models.TextField(blank=True,null=True)
    photo = models.ImageField(upload_to='photos/',verbose_name="kitob rasmi")

    def __str__(self):
        return self.title
