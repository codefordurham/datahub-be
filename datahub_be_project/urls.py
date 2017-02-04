from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from datahub_be_app import views



router = routers.DefaultRouter()
router.register(r'health', views.HealthView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^test/', views.test_view, name='test'),
]
