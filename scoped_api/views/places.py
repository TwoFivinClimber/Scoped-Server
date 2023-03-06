import os
from dotenv import load_dotenv
load_dotenv()
import googlemaps
from django.http import JsonResponse
from django.views.decorators.http import require_GET

gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))



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
    

def city(request):
    options = {
      'input': request.query_params.get('city'),
      'inputtype': 'textquery',
      'fields': ['name', 'formatted_address', 'geometry'],
      'locationbias': 'country:us',
      'language': 'en',
    }
    
    result = gmaps.find_place(**options)
    return JsonResponse(result, safe=False)
  
