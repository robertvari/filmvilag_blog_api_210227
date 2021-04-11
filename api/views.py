from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostSerializer


class PostListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={"request": request})

        return Response(serializer.data)