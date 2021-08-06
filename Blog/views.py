from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth
from .models import Blog
from .forms import CreateBlogForm,UpdateBlogForm
from django.contrib import messages

# Create your views here.
def index(request):
    blogobj = Blog.objects.all()
    return render(request,'index.html',{'blog': blogobj})

def admLogin(request):
    if request.method == 'POST':
        userForm = AuthenticationForm(request=request,data=request.POST)
        if userForm.is_valid():
            uname = userForm.cleaned_data['username']
            pw = userForm.cleaned_data['password']
            usr = auth.authenticate(request,username=uname,password=pw)
            if usr is not None:
                auth.login(request,usr)
                blogobj = Blog.objects.all()
                messages.success(request,'login successfully!')
                return render(request, 'admin.html',{'blog': blogobj})
            else:
                # messages.error(request,"Username or Password is wrong! Please try again..")
                userForm = AuthenticationForm(request=request, data=request.POST)
        else:
            # messages.error(request,"Username or Password is wrong! Please try again..")
            userForm = AuthenticationForm(request=request, data=request.POST)
    else:
        userLogin = AuthenticationForm()
    return render(request,'admlogin.html',{'form':userLogin})

def admindex(request):
    blogobj = Blog.objects.all()
    return render(request,'admin.html',{'blog':blogobj})

def createBlog(request):
    if request.method == 'POST':
        blogForm = CreateBlogForm(request.POST)
        if blogForm.is_valid():
            blogForm.save()
            return redirect('/admindex/')
    else:
        blogForm = CreateBlogForm()
    return render(request,'createBlog.html',{'form':blogForm})

def updateBlog(request,blogid):
    blogObj = Blog.objects.get(Id=blogid)
    if request.method == 'POST':
        upblogForm = UpdateBlogForm(request.POST,instance=blogObj)
        if upblogForm.is_valid():
            blogObj.save()
            messages.success(request,"Blog Updated Successfully!")
            return redirect("/admindex/")
        else:
            upblogForm = UpdateBlogForm(instance=blogObj)
    else:
        blogObj = Blog.objects.get(Id=blogid)
        upblogForm = UpdateBlogForm(instance=blogObj)
    return render(request,'updateBlog.html',{'form':upblogForm})

def deleteBlog(request,blogid):
    blogObj = Blog.objects.get(Id=blogid)
    blogObj.delete()
    messages.success(request,"Blog Deleted Successfully!")
    return redirect("/admindex/")


def logout(request):
    auth.logout(request)
    messages.success(request,"logout Successfully!")
    return redirect("/")
    


