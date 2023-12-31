from django.urls import path
from authentication.views import sign_up_view, sign_in_view, sign_out_view

urlpatterns = [
    path('sign_up/', sign_up_view, name='sign_up'),
    path('sign_in/', sign_in_view, name='sign_in'),
    path('sign_out/', sign_out_view, name='sign_out'),
]