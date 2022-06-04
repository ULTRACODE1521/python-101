import folium
#1
import pandas
data = pandas.read_csv("vol.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
#2
elev = list(data["ELEV"])
map= folium.Map(location=[43.79, -79.35], zoom_start=6, tiles="Stamen Terrain")

fg= folium.FeatureGroup(name="My Map")
#3 add it to the loop
for lt, ln, el in zip(lat,lon, elev):
    #1 delete hi...
    #4 add el to popup but folium needs a number so we conver the el to string
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el), icon=folium.Icon(color="green")))
# you can add popup=str(el),+"m",
map.add_child(fg)

map.save("Map400.html")