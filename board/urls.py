from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.main),
    path('detail/<int:post_id>/', views.detail),
    path('write/', views.write),
]