from ..models import Data

class ChartData(object):    
    def get_data():
        data = {'title': [], 'distance': [],
                 'temperature': [], 'humity': [], 'light': []}

        valves = Data.objects.all()

        for unit in valves:
            data['title'].append(unit.title)
            data['distance'].append(unit.distance)
            data['temperature'].append(unit.temperature)
            data['humity'].append(unit.humity)
            data['light'].append(unit.light)
        
        return data   