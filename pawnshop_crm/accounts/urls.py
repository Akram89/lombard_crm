from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import user_login_view

app_name = 'accounts'

urlpatterns = [
    path('login/', user_login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('create/', register_view, name='create'),   # создать метод

]
