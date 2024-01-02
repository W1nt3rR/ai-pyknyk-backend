from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
import os

from aipyknyk.algorithms import get_agent_steps, get_agent_by_name
from aipyknyk.functions import get_map_by_name

#
@require_http_methods(["GET", "POST"])
@csrf_exempt
def maps_list(request):
    maps = []
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    maps_dir = os.path.join(current_dir, 'maps')

    for file_name in os.listdir(maps_dir):
        file_path = os.path.join(maps_dir, file_name)
        with open(file_path, 'r') as f:
            coins = []

            while True:
                line = f.readline().strip()
                if not len(line):
                    break

                values = [int(val) for val in line.split(',')]
                coins.append({
                    'x': values[0],
                    'y': values[1],
                })

            maps.append({
                'map_name': file_name[:-4],
                'coins': coins,
            })

    return JsonResponse(maps, safe=False)

#
@require_http_methods(["GET", "POST"])
@csrf_exempt
def calculate(request):
    body = request.body

    map = json.loads(body)['map']
    algorithm = json.loads(body)['algorithm']

    try:
        map_path = get_map_by_name(map)
    except Exception as e:
        return JsonResponse({'error': str(e)}).status_code(404)
    
    try:
        agent = get_agent_by_name(algorithm)
    except ValueError as e:
        return JsonResponse({'error': str(e)}).status_code(404)
    
    agent_steps = get_agent_steps(agent, map_path)

    return JsonResponse(agent_steps, safe=False)
