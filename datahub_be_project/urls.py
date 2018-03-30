from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from datahub_be_app import views

router = routers.DefaultRouter()
router.register(r'propsales', views.PropsalesView)
router.register(r'propsales00', views.Propsales00View)
router.register(r'propsales17', views.Propsales17View)
router.register(r'singfamhouse', views.SingfamhouseView)
router.register(r'singfamhouse00', views.Singfamhouse00View)
router.register(r'singfamhouse17', views.Singfamhouse17View)
router.register(r'decrace_bgs_00', views.DECRace_Bgs_00View)
router.register(r'compassrace_bgs_1314', views.CompassRace_Bgs_1314View)
router.register(r'acsrace_bgs_16', views.ACSRace_Bgs_16View)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^test/', views.test_view, name='test'),
]
