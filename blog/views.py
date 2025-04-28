from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages  
from .forms import CommentForm, RatingForm, CoffeePostForm
from .models import CoffeePost, Comment, Rating

# Create your views here.

@login_required
def create_post(request):
    if request.method == "POST":
        post_form = CoffeePostForm(request.POST, request.FILES)
        rating_form = RatingForm(request.POST)

        if post_form.is_valid() and rating_form.is_valid():
            try:
                post = post_form.save(commit=False)
                post.author = request.user
                post.post_rating = rating_form.cleaned_data['stars']
                post.save()

                rating = rating_form.save(commit=False)
                rating.post = post
                rating.user = request.user
                rating.stars = rating_form.cleaned_data['stars']
                rating.save()

                post.update_average_rating()

                messages.success(request, "Your post was created successfully!")
                return redirect("post_detail", slug=post.slug)

            except Exception as e:
                messages.error(request, f"An error occurred while saving your post: {e}")
                return redirect("create_post")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        post_form = CoffeePostForm()
        rating_form = RatingForm()

    return render(request, "blog/create_post.html", {
        "form": post_form,
        "rating_form": rating_form,
    })


class PostList(LoginRequiredMixin, generic.ListView):
    model = CoffeePost
    context_object_name = "posts"
    paginate_by = 9
    template_name = "blog/index.html"
    login_url = "/accounts/login/"  
    redirect_field_name = "next" 

@login_required
def post_detail(request, slug):
    post = get_object_or_404(CoffeePost, slug=slug)
    comments = Comment.objects.filter(post=post)

    comment_form = CommentForm(request.POST or None)
    rating_form = RatingForm(request.POST or None)

    if request.method == "POST":
        if comment_form.is_valid() and request.user.is_authenticated:
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()

        if rating_form.is_valid() and request.user.is_authenticated:
            rating_value = rating_form.cleaned_data['rating']
            Rating.objects.create(
                post=post,
                user=request.user,
                rating=rating_value
            )

        return redirect('post_detail', slug=post.slug)

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

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)