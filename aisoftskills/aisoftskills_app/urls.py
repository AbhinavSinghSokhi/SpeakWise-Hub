
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="indexpage"),
    path('login_signup',views.login_signup, name='login_signup'),
    path('login', views.login_page, name="loginpage"),
    path('signup', views.signup_page, name="signup_page"),
    path('signup_form', views.signup_form, name='signup_form'),
    path('login_form', views.login_form, name="login_form"),
    path('dashboard', views.dashboard_page, name="dashboard"),
    path('logout_user', views.logout_user, name="logout_user"),
    path("user_speech", views.user_speech, name='user_speech'),
    path("contact_us", views.contact_us, name="contact_us"),
    path("about_us", views.about_us, name="about-us"),
]

