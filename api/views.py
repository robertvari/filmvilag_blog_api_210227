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


class AboutView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        about_data = {
            "title": "RÓLUNK",
            "content": "Ez a Filmvilág folyóiratának hivatalos blogja. A szerzőkről.\n\nKérdések, megjegyzések, javaslatok, sajtóanyagok: email."
          }

        return Response(about_data)