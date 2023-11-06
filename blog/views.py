from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class PostCreate(LoginRequiredMixin, CreateView):
 
    # specify the model for create view
    model = Post
 
    # specify the fields to be displayed
 
    fields = "__all__"

    template_name = "blog/post_form.html"

    login_url = "accounts/"
    redirect_field_name = "redirect_to"

class PostUpdateView(LoginRequiredMixin, UpdateView):
    # specify the model you want to use
    model = Post
 
    # specify the fields
    fields = "__all__"
    
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"

    template_name = "blog/postedit_form.html"

    login_url = "accounts/"
    redirect_field_name = "redirect_to"

class PostDeleteView(LoginRequiredMixin, DeleteView):
    # specify the model you want to use
    model = Post
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"

    template_name = "blog/post_confirm_delete.html"

    login_url = "accounts/"
    redirect_field_name = "account/login.html"