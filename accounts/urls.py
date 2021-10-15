from django.urls import path

from .views import SignUpView
from .views import profile_show

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', profile_show, name='profile'),
]
