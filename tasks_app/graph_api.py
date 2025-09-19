import graphene
from graphene_django import DjangoObjectType
from .models import PersonalTask
from graphql import GraphQLError
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class PersonalTaskType(DjangoObjectType):
    assigned_to_user = graphene.Field(UserType)
    class Meta:
        model = PersonalTask
        fields = ("u_id", "title", "status", "assigned_to", "created_at", "updated_at")

    def resolve_assigned_to_user(self, info):
        return self.assigned_to

class Query(graphene.ObjectType):

    personal_tasks = graphene.List(PersonalTaskType)

    def resolve_personal_tasks(self, info):
        user = info.context.user
        if not user or not user.is_authenticated:
            raise GraphQLError("Authentication required")
        
        if not user.is_staff:
            return PersonalTask.objects.filter(assigned_to=user)
        return PersonalTask.objects.all()
    
schema = graphene.Schema(query=Query)
        