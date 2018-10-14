import folium
import pandas



data1 = pandas.read_csv("database.csv")
data = pandas.read_csv("Volcanoes.txt")
data2 = pandas.read_csv("worldcities.csv")

lat1 = list(data1["Latitude"])
lon1 = list(data1["Longitude"])
mag = list(data1["Magnitude"])

lat3=list(data2["lat"])
lon3=list(data2["lng"])
city=list(data2["city"])


lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
	if elevation < 1000:
		return 'green'
	elif 1000<= elevation <3000:
		return 'orange'
	else:
		return 'red'

def color_producer1(mag1):
	print(mag1)

	if mag1 < 4.0:
		return 'yellow'
	elif 5.0<=mag1<=9.0:
		return 'orange'
	else:
		return 'red' 
def color_producer2():
    return 'pink'



map = folium.Map(location=[38.58, -99.09], zoom_start=6,tiles="Mapbox Bright")
'''fga=folium.FeatureGroup(name="AGRICULTURAL LAND")
fga.add_child(folium.GeoJson(data=open('temp.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'red'  if x[0]['Agr_land'] < 10000000
else 'orange' if 10000000 <= x[0]['Agr_land'] < 20000000  else 'blue'}))'''


fge = folium.FeatureGroup(name="EARTHQUAKES")


for lt, ln, el in zip(lat1,lon1,mag):
    fge.add_child(folium.CircleMarker(location=[lt, ln], radius = 7, popup=str(el),
    fill_color=color_producer1(el),
    fill=True, color = 'grey', fill_opacity=0.7))
	
	
	
	
	

	
	
	
	
	
	
	
    

'''
fgair=folium.FeatureGroup(name="CITIES")

print(lat3)
print(lon3)
	

for lt,ln,el in zip(lat3,lon3,city):
    
    
    fgair.add_child(folium.CircleMarker(location=[lt,ln], radius = 7, popup=str(el),
    fill_color='blue',
    fill=True, color = 'grey', fill_opacity=0.7))
	
	'''








fgv = folium.FeatureGroup(name="VOLCANOES")

for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 7, popup=str(el)+"m",
    fill_color=color_producer(el), 
    fill=True, color = 'grey', fill_opacity=0.7))


fgp = folium.FeatureGroup(name="POPULATION")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(fge)
#map.add_child(fgair)
#map.add_child(fga)
map.add_child(folium.LayerControl())

map.save("map2.html")
