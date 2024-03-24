from django.urls import path
from src.applications.foro.views.viewComment import ListComments
from src.applications.foro.views.createComment import CreateComment
app_name = 'foro'
urlpatterns = [
    path('', ListComments.as_view(), name='home'),
    path('create/', CreateComment, name='createComment'),
]
