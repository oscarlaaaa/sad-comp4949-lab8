from django.urls import path 
from .views import homePageView, oscarView, aboutView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('oscar/', oscarView, name='oscar'),
    path('about/', aboutView, name='about'),
    path('homePost/', homePost, name='homePost'),
    path('<int:choice>/results/', results, name='results'),

]