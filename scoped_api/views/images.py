import boto3
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Image, Job

s3 = boto3.resource('s3')
bucket = s3.Bucket('projectscoped')
bucket_name = 'projectscoped'

class ImageView(ViewSet):

    def list(self, request):
        job = request.query_params.get('job')
        if job is not None:
            images = Image.objects.filter(job=job)
        
            images_serialized = ImageSerializer(images, many=True).data
            
            return Response(images_serialized)
          
    def create(self, request):

        image = request.FILES.get('image')
        key = request.data['key']
        
        response = bucket.put_object(Key=key, Body=image.read())
          
        url = f"https://{response.bucket_name}.s3.us-east-2.amazonaws.com/{response.key}"

        image = Image.objects.create(
          image = url,
          job = Job.objects.get(pk = request.data['job']),
          description = request.data['description']
        )
        image.save()
        
        return Response(None, status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        
        image = Image.objects.get(pk=pk)
        
        image.description = request.data['description']
        image.save()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):

        image = Image.objects.get(pk=pk)
        
        key = str(image.image).split('/')[3]
        
        s3.Object(bucket_name, key).delete()
        
        image.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'image', 'description')
        