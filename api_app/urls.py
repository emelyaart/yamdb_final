from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AuthAPIView, CategoryViewSet, CommentViewSet,
                    ConfirmationCodeAPIView, GenreViewSet, ReviewViewSet,
                    TitleViewSet, UsersViewSet)


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/auth/email/', ConfirmationCodeAPIView.as_view()),
    path('v1/auth/token/', AuthAPIView.as_view()),
    path('v1/', include(router.urls)),
]
