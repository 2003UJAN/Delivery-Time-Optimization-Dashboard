import folium
from streamlit.components.v1 import html
from geopy.geocoders import Nominatim

def get_coordinates(place):
    geolocator = Nominatim(user_agent="delivery-dashboard")
    location = geolocator.geocode(place)
    if location:
        return location.latitude, location.longitude
    return None, None

def render_delivery_route(origin, destination):
    lat1, lon1 = get_coordinates(origin)
    lat2, lon2 = get_coordinates(destination)

    if None in [lat1, lon1, lat2, lon2]:
        return html("<b>Could not geocode one or both locations.</b>", height=100)

    m = folium.Map(location=[(lat1 + lat2)/2, (lon1 + lon2)/2], zoom_start=11)
    folium.Marker([lat1, lon1], tooltip="Origin", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker([lat2, lon2], tooltip="Destination", icon=folium.Icon(color="red")).add_to(m)
    folium.PolyLine(locations=[[lat1, lon1], [lat2, lon2]], color='blue', weight=3).add_to(m)

    html_map = m._repr_html_()
    html(html_map, height=400)
