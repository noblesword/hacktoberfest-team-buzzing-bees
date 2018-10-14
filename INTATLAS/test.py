import folium
import pandas


data2 = pandas.read_csv("wcity2.csv")

lat3=list(data2["lat"])
lon3=list(data2["lng"])
city=list(data2["city"])















map = folium.Map(location=[38.58, -99.09], zoom_start=6,tiles="Mapbox Bright")





fgair=folium.FeatureGroup(name="CITIES")

print(lat3)
print(lon3)
	

for lt,ln,el in zip(lat3,lon3,city):
    
    
    fgair.add_child(folium.CircleMarker(location=[lt,ln], radius = 7, popup=str(el),
    fill_color='blue',
    fill=True, color = 'grey', fill_opacity=0.7))
	
	
	
	
map.add_child(fgair)
map.add_child(folium.LayerControl())

map.save("map3.html")