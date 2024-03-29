from django.urls import path
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet, basename='users'),
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
# path("<int:pk>/", PostDetailAPIView.as_view(), name="post_detail"),
# path("", PostListAPIView.as_view(), name="post_list"),
# ]
