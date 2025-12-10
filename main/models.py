from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField('Author', related_name='books')
    genre = models.CharField(max_length=100)
    published_year = models.DateField()
    price = models.PositiveIntegerField()
    desc = models.TextField()
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Meta:
    db_table = 'Book'
    verbose_name = 'Book'
    verbose_name_plural = 'Books'
    ordering = ['-created_at']