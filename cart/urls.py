from django.urls import path
from .views import cart_detail, add_book_to_cart, add_clothes_to_cart, remove_book_from_cart, remove_clothes_from_cart, clear_cart

urlpatterns = [
    path("", cart_detail, name="cart_detail"),
    path("add/book/<int:book_id>/", add_book_to_cart, name="add_book_to_cart"),
    path("add/clothes/<int:clothes_id>/", add_clothes_to_cart, name="add_clothes_to_cart"),
    path("remove/book/<int:book_id>/", remove_book_from_cart, name="remove_book_from_cart"),
    path("remove/clothes/<int:clothes_id>/", remove_clothes_from_cart, name="remove_clothes_from_cart"),
    path("clear/", clear_cart, name="clear_cart"),
]
