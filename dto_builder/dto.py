import graphene
from graphene_django import DjangoObjectType
from weather.models import Reading



class ReadingInputObject(graphene.InputObjectType):
    temperature=graphene.String()
    humidity=graphene.String()
   
    
    
class ReadingOutputObject(graphene.ObjectType):
    id = graphene.ID()
    temperature = graphene.Float()
    humidity=graphene.Float()
    time = graphene.String()