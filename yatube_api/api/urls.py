from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()

router.register('v1/posts', PostViewSet, basename='Post')
router.register('v1/follow', FollowViewSet, basename='Follow')
router.register(r'v1/posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                basename='Comment')
router.register('v1/groups', GroupViewSet, basename='Group')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view, name='token_refresh')
]
