from django.urls import path

from rest_framework.routers import DefaultRouter

from .views.users import RegisterView,LoginView,LogoutView,ProfileView
from .views.category import CategoryView


router = DefaultRouter()
router.register('categories',CategoryView)

urlpatterns =[
  path('users/signup',RegisterView.as_view()) ,
  path('users/login',LoginView.as_view()) ,
  path('users/logout/',LogoutView.as_view()),
  path('users/profile/',ProfileView.as_view())
] + router.urls