from django.urls import path
from .views import hello_world, HelloEthiopia, home

urlpatterns = [
    path('function', hello_world,),
    path('class', HelloEthiopia.as_view(),),
    path('reservation', home )
]