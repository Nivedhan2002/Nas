from django.urls import path, include
from app1 import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login/', views.login_view, name = "login"),
    path('logout/', views.logout_view),
    path('formpage/', views.formpage),
    path('aftersubmit/', views.aftersubmit),
]