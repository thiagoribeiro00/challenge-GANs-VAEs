from django.urls import path
from .views import ContactCreate, ContactDelete

urlpatterns = [
    path('api/contacts/', ContactCreate.as_view(), name='contact-create'),
    path('api/contacts/<int:pk>/', ContactDelete.as_view(), name='contact-delete'),
]
