from django.urls import path

from app.api.views import BasicModelListCreateAPIView

urlpatterns = [
    path("basic-model/", 
         BasicModelListCreateAPIView.as_view(), 
         name="basic-model-list"),
]

