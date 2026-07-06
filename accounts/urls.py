from django.urls import path
from accounts.views import UserCreateAPIView, UserRetrieveUpdateDestroyAPIView


urlpatterns = [
    path(route="accounts/", view=UserCreateAPIView.as_view(), name="account-create-view"),
    path(route="accounts/<int:pk>", view=UserRetrieveUpdateDestroyAPIView.as_view(), name="account-detail-view")
]