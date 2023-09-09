
from django.urls import path,include
from . views import MyUserRegistrationView
from . views import MyUserLoginView

urlpatterns = [
path('register',MyUserRegistrationView.as_view(),name='register'),
path('login',MyUserLoginView.as_view(),name='login'),
#    path('forgetpassword/',MyuserForgetPasswordView.as_view(),name='changepassword'),
]
