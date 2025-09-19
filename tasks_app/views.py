from multiprocessing.managers import Token
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import PersonalTask
from .seralizers import PersonalTaskSerializer
from tasks_app.permitions import IsOwner
from rest_framework.permissions import IsAuthenticated
from graphene_django.views import GraphQLView


# Create your views here.

class TaskApiView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        user = request.user
        tasks = PersonalTask.objects.filter(assigned_to=user)
        serializer = PersonalTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonalTaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def patch(self, request):
        u_id = request.query_params.get("u_id")
        try:
            task = PersonalTask.objects.get(u_id=u_id)
        except PersonalTask.DoesNotExist:
            return Response({"error": "Task not found."}, status=404)
        
        data = request.data.copy()
        serializer = PersonalTaskSerializer(task, data=data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)  
    
    def delete(self, request):
        u_id = request.query_params.get("u_id")
        user = request.user
        try:
            task = PersonalTask.objects.get(u_id=u_id)
        except PersonalTask.DoesNotExist:
            return Response({"error": "Task not found."}, status=404)
        if task.assigned_to != user:
            return Response({"error": "You can only delete your own tasks."}, status=403)   
        
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=204)


class UpdateAuthTokenView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, 'username': user.username, 'email': user.email})
        return Response({"error": "Invalid credentials"}, status=401)
    
class GraphQLApiView(GraphQLView):

    def dispatch(self, request, *args, **kwargs):
        auth = request.META.get("HTTP_AUTHORIZATION")
        if not auth:
            return JsonResponse({"error": "Authentication required"}, status=401)

        parts = auth.split()
        if len(parts) == 2 and parts[0].lower() == "token":
            try:
                token = Token.objects.select_related("user").get(key=parts[1])
                request.user = token.user
            except Token.DoesNotExist:
                return JsonResponse({"error": "Invalid token"}, status=401)
        else:
            return JsonResponse({"error": "Invalid Authorization header"}, status=401)

        return super().dispatch(request, *args, **kwargs)

