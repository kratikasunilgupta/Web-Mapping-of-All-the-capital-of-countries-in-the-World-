import folium
import pandas as pd

map= folium.Map(location=[90,90],zoom_start=6)

data=pd.read_csv("concap.csv")

lat=list(data["CapitalLatitude"])
lon=list(data["CapitalLongitude"])
namc=list(data["CapitalName"])
nam=list(data["CountryName"])



html = """
Capital name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""
fgc=folium.FeatureGroup(name="Capitals")

for lt,ln,nc,ncc in zip(lat,lon,namc,nam):
    iframe=folium.IFrame(html= html % (nc,nc) + "Capital of" +"\n"+ncc, width=150, height=150)
    fgc.add_child(folium.Marker(location =[lt,ln], popup=folium.Popup(iframe) , icon=folium.Icon(color='red')))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding='utf-8-sig').read(),
                             style_function=lambda x:{'fillColor':'green' if x ['properties']['POP2005']<10000000
                                                      else 'orange' if 10000000<x['properties']['POP2005']<20000000
                                                      else 'red'}))
map.add_child(fgc)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")