from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    path("submit_detail_form/", views.submit_detail_form, name="submit_detail_form")
]