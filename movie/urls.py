from rest_framework import routers
from .views import MovieViewSets

app_name = 'movie'
router = routers.DefaultRouter()
router.register('', MovieViewSets)
urlpatterns = router.urls
