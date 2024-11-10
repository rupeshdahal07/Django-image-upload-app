from django.shortcuts import render, redirect
from .models import Image
from .form import Imageform

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Imageform()
    image = Image.objects.all()
    return render(request, 'myapp/home.html', {'form': form, 'images': image})