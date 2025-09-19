"""
URL configuration for personal_tasks_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from tasks_app.views import TaskApiView, UpdateAuthTokenView
from rest_framework.authtoken.views import obtain_auth_token
from tasks_app.views import GraphQLApiView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/signin/", obtain_auth_token, name="signin"),
    path('api-task/', TaskApiView.as_view(), name='api_task'),
    path('api-token-auth/', UpdateAuthTokenView.as_view(), name='api_token_auth'),
    path("graphql/", csrf_exempt(GraphQLApiView.as_view(graphiql=True))),  # GraphQL endpoint
]
