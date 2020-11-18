from django.urls import include, path
from rest_framework import routers
from secretpass import views

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
