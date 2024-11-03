from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:note_id>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("login/", views.login, name="login"),
    path("new/", views.new, name="new"),
    path("logout/", views.logout, name="logout")
]
