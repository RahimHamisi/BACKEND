from weather.schema import WeatherQuery
from weather.views import ReadingMutation
import graphene


class Query(WeatherQuery):
    pass


class Mutation(ReadingMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
