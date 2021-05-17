from django.urls import path
from . import views

app_name = 'yupitter'
urlpatterns = [
    path('top/', views.IndexView.as_view(), name='top'),
]