from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    table = models.SmallIntegerField(default=0)
    no_of_samples = models.SmallIntegerField(default=0)
    low_test_mark = models.SmallIntegerField(default=2)
    upper_test_mark = models.SmallIntegerField(default=2)


    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
    
        
    def __str__(self):
        return self.title
    
class Exercise(models.Model):
    product = models.ForeignKey(Product, related_name='exercises', on_delete=models.CASCADE)
    item_No = models.IntegerField()
    x_val = models.IntegerField()
    y_val = models.IntegerField()
    z_val = models.IntegerField()
    o_val = models.CharField(default='___', max_length=4, blank=True, null=True)
    p_val = models.BooleanField(default=False, null=True, blank=False)
    q_val = models.CharField(default='___', max_length=4, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Exercises'
    
    def __str__(self):
        return f"{self.x_val} X {self.y_val} = {self.z_val}"

    