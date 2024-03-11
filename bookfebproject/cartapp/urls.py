from django.urls import path
from . import views

app_name = 'cartapp'

urlpatterns = [
    path('cartview', views.view_cart, name='cartview'),
    path('add_to_cart/<int:book_id>', views.add_to_cart, name='add_to_cart'),
    # path('unauthenticated/', views.unauthenticated_view, name='unauthenticated'),
]