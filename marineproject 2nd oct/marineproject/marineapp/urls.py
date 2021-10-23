from django.urls import path, include, re_path
from .views import *
# from django_email_verification import urls as mail_urls
from verify_email import urls as mail_urls  #MIGHT HAVE ERROR

app_name = "marineapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LogInView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    # path('verification/', VerificationView.as_view(), name='verify_email'),
    re_path('^send_email/$', sendEmail),
    path('email/', include(mail_urls)),
]