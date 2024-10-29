from rest_framework.routers import DefaultRouter

from .views.users import UserView

router = DefaultRouter()
router.register('users',UserView)

urlpatterns =[
    
] + router.urls