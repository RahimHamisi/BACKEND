import graphene
from dto_builder.dto import ReadingOutputObject
from setting_dto.setting_dto import Builder
# from .models  import Reading


class WeatherQuery(graphene.ObjectType):
    all_readings=graphene.List(ReadingOutputObject)
    
    
    def resolve_all_readings(self,info):
        return Builder.get_all_readings()
    