from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    DownloadPageView
)

urlpatterns =[

    path('', HomePageView.as_view(), name= 'home'),
    path('about/', AboutPageView.as_view(), name= 'about'),
    path('download/', DownloadPageView.as_view(), name= 'download'),
]