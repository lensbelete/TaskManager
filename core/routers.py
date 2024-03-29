from rest_framework import routers

from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet

router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register',RegisterViewSet, basename='register' )
router.register(r'auth/login', LoginViewSet, basename='auth-login')

urlpatterns = [
    *router.urls
]