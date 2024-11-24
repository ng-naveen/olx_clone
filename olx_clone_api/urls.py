from django.contrib import admin
from django.urls import path
from olx_clone_api.views import BikeView, BikeDetailView
urlpatterns = [
    path('bikes/', BikeView.as_view()),
    path('bikes/<int:id>/', BikeDetailView.as_view())
]

