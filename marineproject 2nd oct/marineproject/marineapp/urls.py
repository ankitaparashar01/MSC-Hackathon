from django.urls import path
from .views import *

app_name = "marineapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LogInView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]