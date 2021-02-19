from django.urls import path

from user.api.views import user_views

app_name = 'user'

urlpatterns = [
    path('create/', user_views.CreateUserView.as_view(), name='create'),
    path('token/', user_views.CreateTokenView.as_view(), name='token'),
    path('me/', user_views.ManageUserView.as_view(), name='me'),
]