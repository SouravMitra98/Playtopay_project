from django.urls import path
from .views import PayView

urlpatterns = [
    path("", PayView.as_view()),
]
