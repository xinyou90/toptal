from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'records', views.RecordViewSet)

urlpatterns = [
	url(r'login', obtain_jwt_token),
	url(r'^', include(router.urls)),
]
