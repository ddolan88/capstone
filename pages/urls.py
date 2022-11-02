from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    DownloadPageView,
    Dev1,
    Dev2,
    Dev3,
)

urlpatterns =[

    path('', HomePageView.as_view(), name= 'home'),
    path('dev1/', Dev1.as_view(), name= 'dev1'),
    path('dev2/', Dev2.as_view(), name= 'dev2'),
    path('dev3/', Dev3.as_view(), name= 'dev3'),
    path('about/', AboutPageView.as_view(), name= 'about'),
    path('download/', DownloadPageView.as_view(), name= 'download'),
]