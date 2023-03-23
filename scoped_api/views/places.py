import os
from django.views.decorators.http import require_GET
from django.http import JsonResponse
import googlemaps
from dotenv import load_dotenv
load_dotenv()



gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))


##Locality##
@require_GET
def place(request):
    query = request.GET.get('input', '')
    options = {
    'types': 'establishment',
    'location': 'circle:36.165963, -86.786589',
    'language': 'en',
    } 
    result = gmaps.places_autocomplete(query, **options)
    predictions = [{'label': r['description'], 'value': r['place_id']} for r in result]
    return JsonResponse(predictions, safe=False)


def detail(request):
    place_id = request.GET.get('placeId')
    fields = ['name', 'formatted_address', 'geometry']
    result = gmaps.place(place_id, fields=fields)
    return JsonResponse(result['result'], safe=False)
    
@require_GET
def city(request):
    query = request.GET.get('input', '')
    options = {
    'types': 'locality',
    'location': 'circle:36.165963, -86.786589',
    'language': 'en',
    } 
    result = gmaps.places_autocomplete(query, **options)
    predictions = [{'label': r['description'], 'value': r['place_id']} for r in result]
    return JsonResponse(predictions, safe=False)
  
