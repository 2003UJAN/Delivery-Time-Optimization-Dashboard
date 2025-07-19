import googlemaps

def get_estimated_duration(api_key, origin, destination):
    gmaps = googlemaps.Client(key=api_key)
    try:
        result = gmaps.distance_matrix(origins=[origin],
                                       destinations=[destination],
                                       mode="driving")
        element = result["rows"][0]["elements"][0]
        return {
            "duration_text": element["duration"]["text"],
            "duration_min": element["duration"]["value"] / 60,
            "distance_km": element["distance"]["value"] / 1000
        }
    except Exception as e:
        print("Google Maps error:", e)
        return {
            "duration_text": "N/A",
            "duration_min": None,
            "distance_km": None
        }
