from rest_framework.views import APIView, status

from api.filters import UsernameFilter
from api.models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
  
class PostView(APIView):
    schema = AutoSchema()
    filter_backends = (UsernameFilter,)
    
    def get(self, request):
        params = request.query_params
        name = params.get("name")

        post = Post.objects.all()
        if name:
            post = post.filter(username=name)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def post(self, request):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            saved_post = serializers.save()
            response_data = PostSerializer(saved_post)
            return Response(response_data.data, status=status.HTTP_200_OK)
        return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)