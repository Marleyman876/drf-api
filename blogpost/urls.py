from django.urls import path
from .views import blogpostlist, blogpostdetails

urlpatterns = [
    path('',blogpostlist.as_view(), name='blogpostlist'),
    path('<int:pk>/', blogpostdetails.as_view(),name='blogpostdetails')
    
]
