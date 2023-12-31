from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_safe
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Create your views here.

def maps(request):
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the file
    file_path = os.path.join(current_dir, 'maps/map2.json')

    with open(file_path) as file:
        data = json.load(file)
    return JsonResponse(data)

@require_http_methods(["GET", "POST"])
@csrf_exempt
def calculate(request):
    body = request.body

    # get map from body
    map = json.loads(body)['map']
    algorithm = json.loads(body)['algorithm']

    return JsonResponse({
        'status': 'success',
        'message': 'This is a dummy response',
        'data': {
            'map': map,
            'algorithm': algorithm,
            'body': body.decode('utf-8'),
        }
    })