from django.urls import path

from bookapp import views
app_name = 'bookapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register',views.register,name='register'),
    path('detail/<int:BookId>',views.detail,name='detail'),
    path('trend',views.trending,name='trending'),
    path('discount',views.MegaDiscount,name='MegaDiscount'),
    path('book',views.getBooks,name='getbook'),
    path('category/<int:CategoryId>',views.booksByCategory,name='category'),
    path('author',views.authorList,name='author'),
    path('search',views.search,name='search'),
    path('booksByAuthor/<int:AuthorId>',views.booksByAuthor,name='booksByAuthor'),
    path('Message',views.MessageAddView,name='message'),
]