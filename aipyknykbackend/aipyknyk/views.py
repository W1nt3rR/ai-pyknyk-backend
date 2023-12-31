from django.shortcuts import render
from django.http import JsonResponse
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

def calculate(request):
    headers = request.headers
    body = request.body
    method = request.method
    full_path = request.get_full_path()
    host = request.get_host()

    return JsonResponse({
        'status': 'success',
        'message': 'This is a dummy response',
        'data': {
            'headers': dict(headers),
            'body': body.decode('utf-8'),
            'method': method,
            'full_path': full_path,
            'host': host,
        }
    })