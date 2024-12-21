from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import CoffeePost
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        CoffeePost.objects.create(title=title, description=description, author=request.user)
        return redirect('home')
        return render(request, 'create_post.html')