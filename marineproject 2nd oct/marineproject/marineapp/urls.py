from django.urls import path, include, re_path
from .views import *
from django_email_verification import urls as email_urls
from . import views
# from verify_email import urls as mail_urls  #MIGHT HAVE ERROR

app_name = "marineapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LogInView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("maindashboard/", MainDashboardView.as_view(), name="maindashboard"),
    # path('verification/', VerificationView.as_view(), name='verify_email'),
    re_path('^send_email/$', sendEmail),
    path('email/', include(email_urls)),
    path("hrdashboard/", HRDashboardView.as_view(), name="hrdashboard"),
    path("traineedashboard/",
         TraineeDashboardView.as_view(),
         name="traineedashboard"),
    path("trainerdashboard/",
         TrainerDashboardView.as_view(),
         name="trainerdashboard"),
    path("module1question/",
         Module1QuestionView.as_view(),
         name="module1question"),
    path("module2question/",
         Module2QuestionView.as_view(),
         name="module2question"),
    path("module3question/",
         Module3QuestionView.as_view(),
         name="module3question"),
    path("delete-record/<int:id>", views.delrec),
    path("inside_ship/", InsideShipView.as_view(), name="insideship"),
    path("outside_ship/", OutsideShipView.as_view(), name="Outsideship")
]