from django.shortcuts import render, redirect
from .models import Gallery
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def user_gallery(request):
    user_images = Gallery.objects.all()
    return render(request, 'user_gallery.html', {'user_images': user_images})

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        new_image = Gallery(

            image=image,
            title=title,
            description=description
        )
        new_image.save()

        return redirect('user_gallery')

    return render(request,'upload_image.html')

def delete(request,pk):
        image = Gallery.objects.get(pk=pk)
        image.delete()
        return redirect(user_gallery)


def login_user(req):
    if req.user.is_authenticated:
        return redirect(user_gallery)
    if req.method == 'POST':
         username = req.POST.get('username')
         password = req.POST.get('password')
         if not username or not password:
             messages.error(req, 'Please enter both username and password.')
             return redirect('login')
         user = authenticate(req, username=username, password=password)
         if user is not None:
             login(req, user)
             req.session['username']=user.username
             req.session['user_id']=user.id
             return redirect('user_gallery')
         else:
             messages.error(req, 'Invalid username or password.')
         
    

    return render (req,'login.html')
def signup(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirmpassword')

        if password == confirm_password:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    return render (req,'signup.html')

 
def logout_g(req):
    if 'username' in req.session:
        del req.session['username']
    if 'user_id' in req.session:
        del req.session['user_id']
        

    return render(req,'login.html')
