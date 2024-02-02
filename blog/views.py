from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CommentForm
from .models import reviews


class BlogList(generic.ListView):
    model = reviews
    queryset = reviews.objects.all()
    template_name = "blog/blog_list.html"



class Blog(View):
    """Class & Method to call the post details pages."""

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
            },
        )