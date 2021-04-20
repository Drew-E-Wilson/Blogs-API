from .models import Blogging
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BloggingSerializer
class BloggingViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Blogging.objects.all()
    # The serializer class for serializing output
    serializer_class = BloggingSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]