from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import CoffeePost, Comment
from .forms import CommentForm, RatingForm, CoffeePostForm

# Create your views here.

@login_required
def create_post(request):
    if request.method == "POST":
        form = CoffeePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('user_profile')  
    else:
        form = CoffeePostForm()

    return render(request, 'blog/create_post.html', {'form': form})


class PostList(generic.ListView):
    model = CoffeePost
    context_object_name = 'posts'
    paginate_by = 9
    template_name = "blog/index.html"

@login_required
def post_detail(request, slug):
    post = get_object_or_404(CoffeePost, slug=slug)
    comments = Comment.objects.filter(post=post)

    comment_form = CommentForm(request.POST or None)
    rating_form = RatingForm(request.POST or None)

    if request.method == "POST":
        if comment_form.is_valid() and request.user.is_authenticated:
            # Save the comment
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user  # Assign the logged-in user as the author
            new_comment.save()

        if rating_form.is_valid() and request.user.is_authenticated:
            rating = rating_form.cleaned_data['rating']
            # Logic to handle the rating

        return redirect('blog/post_detail', slug=post.slug)

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'rating_form': rating_form,
    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def user_profile(request):
    user_posts = CoffeePost.objects.filter(author=request.user)
    context = {
        'user': request.user,
        'user_posts': user_posts,
    }
    return render(request, 'blog/user_profile.html', context)
