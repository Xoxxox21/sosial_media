from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import *
# Create your views here.

class Profileview(APIView):
    def get(self,request):
        all_profile = Profile.objects.all()
        return Response({
            'Message': 'List of Profile',
            'Profile List': all_profile
        })
    def post(self, request):
        Profile.objects.create(
            user = self.request,
            id_user = request.data['id_user'],
            bio = request.data['bio'],
            profileimg = request.data['profileimg'],
            location = request.data['location']
        )
        profile = Profile.objects.all().filter(user=request.data['id']).values()
        return Response({
            'Message': 'Profile Add!',
            'Profile': profile
        })