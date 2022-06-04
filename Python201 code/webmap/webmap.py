import folium
map= folium.Map(location=[43.79, -79.35], zoom_start=12, tiles="Stamen Terrain")

fg= folium.FeatureGroup(name="My Map")

for coordinates in[[38.2,-99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi, I am a Marker", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map200.html")