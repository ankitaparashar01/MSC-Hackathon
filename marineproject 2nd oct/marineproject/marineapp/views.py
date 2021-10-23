from django.shortcuts import render, redirect

from django.views.generic import View, TemplateView, CreateView, FormView
from django.views.generic.edit import FormView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, LogInForm

from django.contrib.auth import get_user_model
from verify_email.email_handler import send_verification_email  #MIGHT HAVE ERROR
from django.views.decorators.csrf import csrf_exempt

# from django_email_verification import sendConfirm


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("marineapp:dashboard")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        user = User.objects.create_user(username, email, password)
        form.instance.user = user

        login(self.request, user)

        return super().form_valid(form)


class LogInView(FormView):
    template_name = "login.html"
    form_class = LogInForm
    success_url = reverse_lazy("marineapp:dashboard")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data.get("password")
        usr = authenticate(username=uname, password=pword)

        # if form.is_valid():
        #     inactive_user = send_verification_email(request, form)
        #     inactive_user.cleaned_data['email']
        # Output : test-user123@gmail.com

        if usr is not None and usr.customer:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {
                "form": self.form_class,
                "error": "Invalid Credentials"
            })

        return super().form_valid(form)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("marineapp:home")


class DashboardView(TemplateView):
    template_name = "dashboard.html"


# class VerificationView(TemplateView):
#     #Template_name = "my_custom_email_message.html"
#     pass


@csrf_exempt
def sendEmail(form, request):
    # username = request.POST.get('username')
    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password")
    email = form.cleaned_data.get("email")
    user = get_user_model().objects.create(username=username,
                                           password=password,
                                           email=email)
    # sendConfirm(user)
    send_verification_email(user)
    return render(request, 'confirm_template.html')