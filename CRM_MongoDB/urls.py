from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
router = DefaultRouter()

router.register('User',views.UserViewSet,basename='user'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
	# path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
 #    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
