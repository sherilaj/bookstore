from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True, editable=False)
    RefId = models.CharField(max_length=50, blank=True, null=True)
    CategoryName = models.CharField(max_length=300,blank=True, null=True)
    CategoryIcon = models.FileField(
        blank=True, null=True, upload_to='category/icon')
    CategoryImage = models.FileField(
        blank=True, null=True, upload_to='category/image')
    Description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.CategoryName
    
class Author(models.Model):
    AuthorId = models.AutoField(primary_key=True,editable=False)
    AuthorName = models.CharField(max_length=20,null=True,blank=True)
    AuthorImage = models.FileField(upload_to='author')
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.AuthorName
  
class Book(models.Model):
    BookId = models.AutoField(primary_key=True,editable=False)
    Title = models.CharField(max_length=30,blank=True,null=True)
    Description = models.TextField(blank=True, null=True)
    Authors = models.ForeignKey(Author,on_delete=models.CASCADE)
    BookCoverImage = models.FileField(
        blank=True, null=True, upload_to='book/cover')
    BookCoverImageAlternativeText=models.TextField(blank=True, null=True)
    
    Stock = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    DiscountPercent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    OfferPrice = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    
    Categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    SubCategory = models.CharField(blank=True, null=True, max_length=50)
    SEOTitle = models.CharField(max_length=50,blank=True,null=True)
    SEOKeyword = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.Title
    


class BookRating(models.Model):
    BookRatingId = models.AutoField(primary_key=True, editable=False)
    Books = models.ForeignKey(Book,on_delete=models.CASCADE)
    User = models.CharField(blank=True, null=True, max_length=50)
    Rating = models.IntegerField(default=0)
    Feedback = models.TextField(blank=True, null=True)
    RatingOn = models.DateTimeField(editable=False, default=datetime.now)
    
class Message(models.Model):
    SortId=models.DateTimeField(editable=False, default=datetime.now)
    MessageId = models.AutoField(primary_key=True, editable=False)
    Name=models.CharField(max_length=300,blank=False)
    EmailId=models.CharField(max_length=150,blank=False)
    Message=models.TextField(blank=False)
    Subject=models.TextField(null=True,blank=True)

