from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# dummy
# from django.views.generic import ListView
from home.models import Contact
from django.contrib.auth.forms import UserCreationForm
from home.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .models import Destination


# from django.views.generic import ListView, CreateView # new
# from django.urls import reverse_lazy # new

# from home.forms import ImageForm # new

# dummy

# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            # check if user has entered correct credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/")

            else:
                # No backend authenticated the credentials
                messages.info(request, 'Username OR password is incorrect')
                return render(request, 'login.html')

        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")


# dummy1
# def contact(request):
#    if request.method=="POST":
#        name=request.POST.get('name')
#        image=request.POST.get('image')
#        contact=Contact(name=name,image=image)
#        contact.save()
#        messages.success(request, 'Your message has been sent!')
#    return render(request,"contact.html")

# def contact(request):
#    lastimage=Contact.objects.last()
#    image=lastimage.image

#    form=ImageForm(request.POST or None, request.FILES or None)
#    if form.is_valid():
#        form.save()

#    context={'image':image, 'form':form}

#    return render(request, 'contact.html', context)

# def contact(request):
# if request.method =='POST':
# form=ImageForm(request.POST, request.FILES)
# if form.is_valid():
# form.save()
# img_obj=form.instance
# return render(request, 'contact.html', {'form':form, 'img_obj':img_obj})
# else:
# form= ImageForm()
# return render(request, 'contact.html', {'form':form})

def blog(request):
    dests = Destination.objects.all()

    return render(request, "blog.html", {'dests': dests})


@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        ApplicationNumber = request.POST.get('ApplicationNumber')
        Percentile = request.POST.get('Percentile')
        Address1 = request.POST.get('Address1')
        file = request.FILES["file"]
        file1 = request.FILES["file1"]
        document = Contact.objects.create(name=name, father=father, mother=mother,
                                          email=email, phone=phone, ApplicationNumber=ApplicationNumber,
                                          Percentile=Percentile,
                                          Address1=Address1, file=file, file1=file1)
        document.save()
        messages.success(request, 'Your message has been sent!')
        messages.success(request, 'Your message has been sent!')
    return render(request, "contact.html")
# dummy1

# dummy
# class HomePageView(ListView):
#    model = Post
#    template_name = 'index.html'


# class HomePageView(ListView):
#    model = Post
#    template_name = 'index.html'

# class CreatePostView(CreateView): # new
#    model = Post
#    form_class = PostForm
#    template_name = 'post.html'
#    success_url = reverse_lazy('index')
# dummy
