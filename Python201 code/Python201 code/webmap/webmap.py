import folium
map= folium.Map(location=[43.79, -79.35], zoom_start=12, tiles="Stamen Terrain")
fg= folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[43.79324669883864, -79.35320379493692], popup="Hi, I am a Marker", icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("Map1000.html")