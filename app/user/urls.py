from django.urls import path
from .views import CreateTokenView

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
]
