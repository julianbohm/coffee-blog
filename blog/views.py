from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import CoffeePost

# Create your views here.

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        CoffeePost.objects.create(title=title, description=description, author=request.user)
        return redirect('home')
        return render(request, 'create_post.html')



class PostList(ListView):
    queryset = CoffeePost.objects.all()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = "blog/index.html"

    def get_queryset(self):
        queryset = CoffeePost.objects.all()
        return queryset