from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from src.applications.foro.models.comment import Comment
def CreateComment(request):
    """
    Create a new comment.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is 'POST', creates a new comment with the provided data and redirects to the home page.
        If the request method is not 'POST', renders the 'create_comment.html' template.

    """
    if request.method == 'POST':
        name_user = request.POST.get('name_user')
        title_post = request.POST.get('title_post')
        description_post = request.POST.get('description_post')
        nuevo_post = Comment.objects.create(
            name_user=name_user,
            title_post=title_post,
            description_post=description_post
        )
        nuevo_post.save()
        return redirect(reverse_lazy('foro:home'))
    else:
        return render(request, 'foro/create_comment.html')
    