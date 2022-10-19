from django.urls import path
from community import views
from .views import (
    CommunityPageView
)

urlpatterns =[
    path('community/', CommunityPageView.as_view(), name= 'community_posts'),
    path("new/", views.PostCreateView.as_view(), name = 'post_new'),
    path('<int:pk>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('<int:pk>/', views.PostDeleteView.as_view(), name = 'post_delete'),
]