# coding: utf-8

from rest_framework import routers
from .views import AuthorViewSet, BookViewSet


router = routers.DefaultRouter()
router.register(r'auther', AuthorViewSet)
router.register(r'book', BookViewSet)