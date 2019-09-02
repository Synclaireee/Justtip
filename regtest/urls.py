from django.urls import path
from regtest import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('r/', views.R_List.as_view()),
    path('r/<int:pk>/', views.R_Detail.as_view()),
    path('l/',views.L_Detail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)