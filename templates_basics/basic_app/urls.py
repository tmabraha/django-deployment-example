from django.urls import path
from basic_app import views

# TEMPLATE TAGGING - first step is to create a global variable equal to the app name
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]
