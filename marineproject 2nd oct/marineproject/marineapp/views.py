from django.shortcuts import render, redirect

from django.views.generic import View, TemplateView, CreateView, FormView
from django.views.generic.edit import FormView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, LogInForm



# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("marineapp:home")

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

    def displaydepartment(request):
        display = Customer.objects.department.get()


   

   