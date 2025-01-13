from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
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


class PostList(generic.ListView):
    model = CoffeePost
    context_object_name = 'posts'
    paginate_by = 9
    template_name = "blog/index.html"

@login_required
def post_detail(request, slug):
    post = get_object_or_404(CoffeePost, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def user_profile(request):
    user_posts = CoffeePost.objects.filter(author=request.user)
    context = {
        'user': request.user,
        'user_posts': user_posts,
    }
    return render(request, 'blog/user_profile.html', context)
