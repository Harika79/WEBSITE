from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class News(models.Model):
       title=models.CharField(primary_key=True, max_length=200 )
       author = models.CharField(max_length=200 )
       date = models.DateField()
       content = models.TextField()


from django.db import models

# Create your models here.
# models.py
# from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='purchased_book_images/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='book_pdfs/', null=True, blank=True)
    email = models.EmailField(max_length=254, default='ex@gmail.com')  # Added email field
    def __str__(self):
        return self.title

class PurchaseDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit_card = models.CharField(max_length=16, default=123566) 
    timestamp = models.DateTimeField(default=timezone.now)


    