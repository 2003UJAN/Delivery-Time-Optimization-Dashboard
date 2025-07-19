import googlemaps

def get_route_duration(gmaps_api_key, origin, destination):
    gmaps = googlemaps.Client(key=gmaps_api_key)
    result = gmaps.distance_matrix(origins=[origin],
                                    destinations=[destination],
                                    mode='driving')
    duration = result['rows'][0]['elements'][0]['duration']['text']
    return duration
