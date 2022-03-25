from blog.views import frontpage
from django.urls import path

urlpatterns = [
    path('', frontpage, name='frontpage'),
]