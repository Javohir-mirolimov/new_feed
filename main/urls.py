from django.urls import path
from .views import *

urlpatterns = [
    path('', open_view, name='open_url'),
    path('create-user', ac_create_view, name='user_create_url'),
    path('my-account', my_account_view, name='my_account_url'),
    path('index-view/', index_view, name="index_view_url"),
]