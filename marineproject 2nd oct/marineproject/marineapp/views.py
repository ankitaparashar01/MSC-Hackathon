from django.shortcuts import render, redirect

from django.views.generic import View, TemplateView, CreateView, FormView
from django.views.generic.edit import FormView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from .forms import *

# from verify_email.email_handler import send_verification_email  #MIGHT HAVE ERROR
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import get_user_model
from django_email_verification import send_email


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("marineapp:maindashboard")

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
    success_url = reverse_lazy("marineapp:maindashboard")

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


class MainDashboardView(TemplateView):
    template_name = "maindashboard.html"


class HRDashboardView(TemplateView):
    template_name = "hrdashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['names_list'] = Customer.objects.all()

        return context


class TraineeDashboardView(TemplateView):
    template_name = "traineedashboard.html"


class TrainerDashboardView(TemplateView):
    template_name = "trainerdashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['module1_list'] = Module1.objects.all()
        context['module2_list'] = Module2.objects.all()
        context['module3_list'] = Module3.objects.all()
        context['module4_list'] = Module4.objects.all()
        context['module5_list'] = Module5.objects.all()

        return context


def delrec(request, id):
    delete_row = Module1.objects.get(id=id)
    delete_row.delete()
    module1_list = Module1.objects.all()

    return render(request, "trainerdashboard.html", {"Module1": module1_list})


class Module1QuestionView(CreateView):
    template_name = "module1.html"
    form_class = Module1Form
    success_url = reverse_lazy("marineapp:trainerdashboard")

    def form_valid(self, form):

        return super().form_valid(form)


class Module2QuestionView(CreateView):
    template_name = "module2.html"
    form_class = Module2Form
    success_url = reverse_lazy("marineapp:trainerdashboard")

    def form_valid(self, form):

        return super().form_valid(form)


class Module3QuestionView(CreateView):
    template_name = "module3.html"
    form_class = Module3Form
    success_url = reverse_lazy("marineapp:trainerdashboard")

    def form_valid(self, form):

        return super().form_valid(form)


class Module4QuestionView(CreateView):
    template_name = "module4.html"
    form_class = Module4Form
    success_url = reverse_lazy("marineapp:trainerdashboard")

    def form_valid(self, form):

        return super().form_valid(form)


class Module5QuestionView(CreateView):
    template_name = "module5.html"
    form_class = Module5Form
    success_url = reverse_lazy("marineapp:trainerdashboard")

    def form_valid(self, form):

        return super().form_valid(form)


class MatchInstructionView(TemplateView):
    template_name = "matchinstruction.html"


class InsideShipView(TemplateView):
    template_name = "Inside_Ship.html"
    pass


class OutsideShipView(TemplateView):
    template_name = "Outside_Ship.html"
    pass


class VirtualTourView(TemplateView):
    template_name = "virtualtourmain.html"
    pass


# class VerificationView(TemplateView):
#     #Template_name = "my_custom_email_message.html"
#     pass


# @csrf_exempt
def sendEmail(request):  #add 'form' if required
    # username = form.cleaned_data.get("username")
    username = request.POST.get('username')
    password = request.POST.get("password")
    email = request.POST.get("email")
    user = get_user_model().objects.create(username=username,
                                           password=password,
                                           email=email)
    user.is_active = False
    # sendConfirm(user)
    send_email(user)
    send_email(user, custom_salt=my_custom_key_salt)
    return render(request, 'confirm_template.html')


class MyClassView(FormView):
    def form_valid(self, form):
        user = form.save()
        returnVal = super(MyClassView, self).form_valid(form)
        send_email(user)
        return returnVal
