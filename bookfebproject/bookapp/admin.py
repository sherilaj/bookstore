from django.contrib import admin
from . models import Book, BookRating, Category, Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('BookId',
            'Title',
            'Description',
            'Authors',
            'BookCoverImage',
            'BookCoverImageAlternativeText',
            'Stock',
            'UnitPrice',
            'DiscountPercent',
            'OfferPrice',
            'Categories',
            'SubCategory',
            'SEOTitle',
            'SEOKeyword',
        )
    def save_model(self, request, obj, form, change):
        # Calculate the offer price before saving the object
        discount_amount = (obj.UnitPrice * obj.DiscountPercent) / 100
        obj.OfferPrice = obj.UnitPrice - discount_amount
        super().save_model(request, obj, form, change)

admin.site.register(Book,BookAdmin)


class BookRatingAdmin(admin.ModelAdmin):
    list_display = (
            'BookRatingId',
            'Books',
            'User',
            'Rating',
            'Feedback',
            'RatingOn')
admin.site.register(BookRating,BookRatingAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
            'CategoryId',
            'RefId',
            'CategoryName',
            'CategoryIcon',
            'CategoryImage',
            'Description',
        )
admin.site.register(Category,CategoryAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('AuthorId',
                    'AuthorName',
                    'AuthorImage',
                    'Category',
                    )
admin.site.register(Author,AuthorAdmin)