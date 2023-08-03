from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create an instance of the DefaultRouter class
router = DefaultRouter()

# Register your viewset with a prefix and a basename
router.register('chatbot', views.ChatbotViewSet, basename='chatbot')

# Create a list of urlpatterns that contains the router.urls attribute
urlpatterns = router.urls

