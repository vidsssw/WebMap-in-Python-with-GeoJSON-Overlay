import folium
html = """<h4>Name: %s </h4>
"""


m=folium.Map(location=[18.5204,73.8567])
fg1=folium.FeatureGroup(name="Places")
coordinates=[[18.564332,73.777535],[18.569250,73.776047],[18.516679,73.879337],[18.511544,73.820473],[18.567171,73.807642]]
colors=["red","green","orange","blue","purple"]
names=["World of Desserts","London Dock Cafe","Marz O Rin","Ganache","Superheroes Cafe"]

for i in range (0,5):
    iframe = folium.IFrame(html=html % str(names[i]), width=200, height=100)
    fg1.add_child(folium.Marker(location=coordinates[i], icon=folium.Icon(color=colors[i]), popup=folium.Popup(iframe)))
fg2=folium.FeatureGroup(name="Population")
f=open("world.json","r+",encoding='utf-8-sig')
fg2.add_child(folium.GeoJson(data=f.read(),style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<5000000 else 'orange'}))
m.add_child(fg1)
m.add_child(fg2)

m.add_child(folium.LayerControl())
m.save('map.html')