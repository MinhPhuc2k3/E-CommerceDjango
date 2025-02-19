from django.urls import path
from .views import login_view, register_view
from .views import logout_view
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name="logout"),
]
