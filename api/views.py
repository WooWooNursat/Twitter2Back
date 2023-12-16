from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Post
from rest_framework import status, generics
from .serializers import PostSerializer
from rest_framework.response import Response


class PostListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        ser = PostSerializer(posts, many=True)
        return Response(ser.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        ser = PostSerializer(request.data)
        if ser.is_valid():
            ser.save()

            return Response(status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

