from django.urls import path
from .views import  Images,Prism
from django.urls import path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'',Images,basename='')
router = DefaultRouter()
router.register(r'',Prism,basename='')

urlpatterns = [
    
    path('', Images.as_view(),name='image'),
    path('prism', Prism.as_view(),name='prism')

    
]



