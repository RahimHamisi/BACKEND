import graphene
from weather.models import Reading
from dto_builder.dto import ReadingInputObject, ReadingOutputObject


class Builder:
    
    
 def get_all_readings():
    readings = Reading.objects.all()
    all_readings = []
    for data in readings:
        output = ReadingOutputObject(
            id=data.id,
            temperature=data.temperature,
            time=data.time # Ensure the time is in a string format
            
        )
        all_readings.append(output)
        print(all_readings)
    return all_readings

    
   