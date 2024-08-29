
import graphene
from dto_builder.dto import *
from setting_dto.setting_dto import *

 
# Create your views here. 
class CreateWeatherData(graphene.Mutation):
    class Arguments:
        input = ReadingInputObject()

    reading = graphene.Field(ReadingOutputObject)
    success = graphene.Boolean()

    def mutate(self, info, input):
        reading = Reading.objects.create(
            temperature=input.temperature,
            # humidity=input.humidity# Ensure this matches your model field
        )
        print(reading.temperature)
        return CreateWeatherData(reading=reading, success=True)
    
class ReadingMutation(graphene.ObjectType):
    create_reading = CreateWeatherData.Field()
        
            
        

