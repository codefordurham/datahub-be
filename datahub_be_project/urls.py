from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from datahub_be_app import views

router = routers.DefaultRouter()
router.register(r'ltdbacs_trts_7016', views.LTDBACS_trts_7016View)
router.register(r'bgs9800', views.bgs9800View)
router.register(r'bgs1318', views.bgs1318View)
router.register(r'durhamhds', views.durhamhdsView)
router.register(r'muniboundaries', views.muniboundariesView)
router.register(r'cntyboundaries', views.cntyboundariesView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^test/', views.test_view, name='test'),
]
