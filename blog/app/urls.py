from django.urls import path

from rest_framework.routers import DefaultRouter

from .views.users import RegisterView,LoginView,LogoutView


router = DefaultRouter()
# router.register('users',UserView)

urlpatterns =[
  path('users/signup',RegisterView.as_view()) ,
  path('users/login',LoginView.as_view()) ,
  path('users/logout/',LogoutView.as_view())
] + router.urls