from rest_framework import routers
from .api import ServicioviewSet


router = routers.DefaultRouter()
router.register('api/apiservicio',ServicioviewSet, 'apiservicio')

urlpatterns = router.urls