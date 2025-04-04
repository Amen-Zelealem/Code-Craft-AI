from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("suggest/", views.suggest, name="suggest"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("past/", views.past, name="past"),
    path("delete_past_codes/<Past_id>",views.delete_past_code,name="delete_past_code")
]
