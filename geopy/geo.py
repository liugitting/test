import folium

map_center=[31.2304,121.4737]

my_map=folium.Map(location=map_center,zoom_start=12)

folium.Marker(
    map_center,
    popup="SHANGHAI",
    icon=folium.Icon(color="blue",icon="info-sign")
).add_to(my_map)

my_map.save("my_map.html")