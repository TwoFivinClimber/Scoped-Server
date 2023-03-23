from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Blog, User, Company

class BlogView(ViewSet):
  
    def list(self, request):

        cid = request.query_params.get('cid')
        
        if cid is not None:

            blogs = Blog.objects.filter(company = cid)
        
        blogs_serialized = BlogSerializer(blogs, many=True).data
        
        return Response(blogs_serialized, status.HTTP_200_OK)
    
    def create(self, request):

        post = Blog.objects.create(
          uid = User.objects.get(pk = request.data['uid']),
          company = Company.objects.get(pk = request.data['cid']),
          title = request.data['title'],
          content = request.data['content'],
          datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        post.save()
        
        return Response(None, status.HTTP_201_CREATED)
      
    def update(self, request, pk):

        post = Blog.objects.get(pk=pk)
        post.title = request.data['title']
        post.content = request.data['content']
        post.datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        post.save()
        
        return Response(None, status.HTTP_202_ACCEPTED)
      
    def destroy(self, request, pk):
        
        post = Blog.objects.get(pk=pk)
        post.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)

class BlogSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'datetime', 'uid',)
        depth = 1
        