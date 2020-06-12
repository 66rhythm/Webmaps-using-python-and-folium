import folium
import pandas
data=pandas.read_csv("original.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
elev= list(data["ELEV"])

def color_producer(elev):

    if elev>3000:
        return 'green'
    elif elev<3000 and elev>2000:
        return 'red'    
    else:
        return 'blue'
   

map=folium.Map(location=[80,-100],zoom_start=6 ,tiles="Stamen Terrain")
fgv=folium.FeatureGroup(name="Volcanoes")



for lt,ln,elev in zip(lat , lon ,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln] , radius=6, popup=str(elev)+"m" , fill_color=color_producer(elev) ,color='grey' ,fill=True, fill_opacity=0.6))


fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json' ,'r', encoding='utf-8-sig' ).read(),
style_function=lambda x: {'fillColor':'black' if x['properties']['POP2005']<1000000 
else 'orange' if 1000000<=x['properties']['POP2005']<2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
