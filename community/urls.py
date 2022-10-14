from django.urls import path
from .views import (
    CommunityPageView
)

urlpatterns =[
    path('community/', CommunityPageView.as_view(), name= 'community_posts')
]