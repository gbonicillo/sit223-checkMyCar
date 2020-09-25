from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("makes/", views.MakeList.as_view()),
    path("makes/<int:pk>", views.MakeDetail.as_view()),
    path("makes/<int:pk>/update", views.MakeUpdate.as_view()),
    path("makes/create", views.MakeCreate.as_view()),
    path("cars/", views.CarList.as_view()),
    path("cars/<int:pk>", views.CarDetail.as_view()),
    path("cars/<int:pk>/update", views.CarUpdate.as_view()),
    path("cars/create", views.CarCreate.as_view()),
    path("reports/", views.IssueList.as_view()),
    path("reports/<int:pk>", views.IssueDetail.as_view()),
    path("reports/<int:pk>/update", views.IssueUpdate.as_view()),
    path("reports/create", views.IssueCreate.as_view()),
    path("auth/user", views.AuthUserDetail.as_view()),
    path("auth/user/update/<int:pk>", views.AuthUserUpdate.as_view()),
    path("auth/user/change-password/<int:pk>", views.AuthUserUpdatePassword.as_view()),
    path("auth/register", views.AuthUserRegister.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)