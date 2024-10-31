from django.urls import path

from rest_framework.routers import DefaultRouter

from .views.users import RegisterView,LoginView,LogoutView,ProfileView
from .views.category import CategoryView
from .views.blog import BlogView
from .views.comment import CommentView
from .views.likes import BlogLikeView,CommentLikeView


router = DefaultRouter()
router.register('categories',CategoryView)
router.register('blogs',BlogView)
router.register('comments',CommentView)
router.register('blog-likes',BlogLikeView)
router.register('comment-likes',CommentLikeView)


urlpatterns =[
  path('users/signup',RegisterView.as_view()) ,
  path('users/login',LoginView.as_view()) ,
  path('users/logout/',LogoutView.as_view()),
  path('users/profile/',ProfileView.as_view())
] + router.urls