from django.urls import path
from . import views as authviews


urlpatterns = [
    path('', authviews.index, name='home'), 
]