import googlemaps
from django.http import JsonResponse
from django.views.decorators.http import require_GET



@require_GET
def place(request):
    query = request.GET.get('input', '')
    gmaps = googlemaps.Client(key='AIzaSyCJ2NfeSz1_2urbi7pZUOEobxy7plkKNxA')
    options = {
    'types': 'establishment',
    'location': 'circle:36.165963, -86.786589',
    'language': 'en',
    } 
    result = gmaps.places_autocomplete(query, **options)
    predictions = [{'description': r['description'], 'place_id': r['place_id']} for r in result]
    return JsonResponse(predictions, safe=False)
    

def city(request):
    gmaps = googlemaps.Client(key='AIzaSyCJ2NfeSz1_2urbi7pZUOEobxy7plkKNxA')
    options = {
      'input': request.query_params.get('city'),
      'inputtype': 'textquery',
      'fields': ['name', 'formatted_address', 'geometry'],
      'locationbias': 'country:us',
      'language': 'en',
    }
    
    result = gmaps.find_place(**options)
    return JsonResponse(result, safe=False)
  
