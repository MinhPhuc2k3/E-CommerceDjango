from django.urls import path
from .views import product_list_view, book_detail_view, clothes_detail_view

urlpatterns = [
    path("all/", product_list_view, name="product-list"),
    path("book/<int:book_id>/", book_detail_view, name="book-detail"),
    path("clothes/<int:clothes_id>/", clothes_detail_view, name="clothes-detail"),
]
