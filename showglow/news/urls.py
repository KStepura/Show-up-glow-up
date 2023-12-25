from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('<int:pk>', views.TrackerDetailView.as_view(), name='news-detail'),
]
