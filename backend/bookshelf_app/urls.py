from rest_framework import routers, urlpatterns
from bookshelf_app.views import BookViewSet

router = routers.DefaultRouter()
router.register('', BookViewSet, basename='book')
urlpatterns = router.urls

print(urlpatterns)