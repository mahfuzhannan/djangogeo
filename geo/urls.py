from rest_framework import routers

from geo.views import GeoPointViewSet

router = routers.DefaultRouter()
router.register(r'points', GeoPointViewSet)

urlpatterns = router.urls