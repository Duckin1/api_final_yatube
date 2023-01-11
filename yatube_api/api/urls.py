from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router_v1 = DefaultRouter()

router_v1.register('follow', FollowViewSet, basename='Follow') 
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                   basename='comments')
router_v1.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
