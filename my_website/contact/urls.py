from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_me_test, name='test-page'),
]
