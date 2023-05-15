from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from insurance import views

router = DefaultRouter()
router.register('user/', views.User)
router.register('policy/', views.Policy)
router.register('claim/ ', views.Claim)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls))
]
