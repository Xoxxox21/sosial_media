from django.urls import path
from . import views

urlpatterns = [
    path("Api_profile/", views.Profileview.as_view())
]
