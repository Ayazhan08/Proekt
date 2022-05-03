from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .models import *
from .forms import *
from django.conf import settings



# Create your views here.
def hello(request):
    return render(request, 'posts/hello.html')


def index(request):
    return render(request, 'posts/index.html')


# def show_post(request,post_id):
#     post=get_object_or_404(Labs, pk=post_id)
#     context={'post':post}
#     return render(request,'posts/post.html',context=context)

def show_post1(request, post_slug):
    post = get_object_or_404(Mids, slug=post_slug)
    context = {'post': post}
    return render(request, 'posts/post.html', context=context)


def register_done(request):
    new = Registration.objects.order_by('-id')[:1]
    return render(request, 'posts/registration_done.html', {'news': new})

def registration(request):

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('register_done')
    else:
        form = AddPostForm()
    return render(request, 'posts/registration.html',{'form': form,'title': 'registration'})



class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'posts/susccessfull.html'

    def get(self, request):
        form = self.form_class()
        return render(request,'posts/successfull.html',{'email_form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, 'posts/successfull.html',
                              {'email_form': form, 'error_message': 'Электрондық пошта мекенжайына жіберілді %s' % email})
            except:
                return render(request, 'posts/successfull.html',
                              {'email_form': form, 'error_message': 'Не тіркеме тым үлкен немесе бүлінген'})

        return render(request, 'posts/successfull.html',
                      {'email_form': form, 'error_message': 'Электрондық поштаны жіберу мүмкін емес. Тағы жасауды сәл кейінірек көріңізді өтінеміз'})

class RegisterUser(CreateView):
        form_class = RegisterUserForm
        template_name = 'posts/register.html'
        success_url = reverse_lazy('login')


def login_user(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.success(request, ("There is some problem .. Try again.."))
                return redirect('login')
        else:
            return render(request, 'posts/login.html', {})

def logout_user(request):
        logout(request)
        return redirect('login')