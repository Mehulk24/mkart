from django.db import models
from django.contrib.auth.models import User

# Create your models here.
choice_product = (
    ("Man_tending_page","treding_man"),
    ("Woman_tending_page","treding_woman"),
    ("Kids_tending_page","treding_kids"),
    ("Man","man"),
    ("Woman","woman"),
    ("Kids","kids"),
)

card_op = (
    ("man-product","Man"),
    ("woman-product","woman-product"),
    ("kids-product","kids-product"),
)
class Product(models.Model):
    product_id = models.AutoField
    p_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,choices=choice_product,default=" ")
    subCategory = models.CharField(max_length=50,default="")
    p_price = models.IntegerField(default=0)
    des = models.TextField(max_length=300)
    product_date = models.DateField()
    p_img1=models.ImageField(upload_to="img",default="") 
    p_img2=models.ImageField(upload_to="img",default="") 
    
    def __str__(self):
        return self.p_name
    
class Ladeng_page(models.Model):
    page_name = models.CharField(max_length=50,default="")
    page_de= models.TextField(max_length=500,default="")
    page_img= models.ImageField(upload_to="img",default="")
    
    def __str__(self):
        return self.page_name

class logo(models.Model):
    logo=models.ImageField(upload_to="img",default="")
    
class c_product(models.Model):
    c_name=models.CharField(default="", max_length=50)
    category = models.CharField(max_length=50,choices=card_op,default=" ")
    c_des=models.TextField(default="", max_length=500)
    c_img=models.ImageField(upload_to="img",default="")
    
    def __str__(self):
        return self.c_name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    
    def image(self):
        return self.product.p_img1.url

    def __str__(self):
        return self.product.p_name

    
    
    
    
