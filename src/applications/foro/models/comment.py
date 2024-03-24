from django.db import models
class Comment(models.Model):
    """
    Represents a comment on a post in the forum.
    """

    name_user = models.CharField(max_length=255)
    title_post = models.CharField(max_length=255)
    description_post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        This class provides metadata options for the Comment model.
        """
        app_label = 'foro'

    def __str__(self):
        """
        Returns a string representation of the Comment object.
        
        The string representation is the name of the user who made the comment.
        
        Returns:
            str: The name of the user who made the comment.
        """
        return str(self.name_user)
    
