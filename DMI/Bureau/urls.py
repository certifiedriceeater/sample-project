from django.urls import path
from . import views

urlpatterns = [
    path('Bureau/', views.Bureau, name='Bureau'),
    path('Bureau/details,<int:id>', views.details, name='details')
]