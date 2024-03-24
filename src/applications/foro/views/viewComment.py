from django.views.generic import ListView
from src.applications.foro.models.comment import Comment

class ListComments(ListView):
    """
    A view for listing comments.

    This view extends the Django ListView class and is used to display a list of comments.
    It retrieves the comments from the database and filters them based on a search query if provided.

    Attributes:
        model (Model): The model class representing the comments.
        template_name (str): The name of the template used to render the view.
        context_object_name (str): The name of the variable used to store the comments in the template context.
    """

    model = Comment
    template_name = "foro/home.html"
    context_object_name = 'list_elements'

    def get_queryset(self):
        """
        Get the queryset of comments.

        This method is called to retrieve the comments from the database.
        If a search query is provided in the request parameters, it filters the comments based on the query.
        Otherwise, it returns all the comments.

        Returns:
            QuerySet: The queryset of comments.
        """
        query = self.request.GET.get('text')
        if query:
            return Comment.objects.filter(name_user__icontains=query)
        else:
            return Comment.objects.all()
