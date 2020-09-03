from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("cars/", views.CarList.as_view()),
    path("cars/<int:pk>", views.CarDetail.as_view()),
    path("auth/user", views.AuthUserDetail.as_view()),
    path("auth/register", views.AuthUserRegister.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)