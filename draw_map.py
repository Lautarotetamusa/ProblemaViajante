import folium

mapa_path = "ruta.html"

coordenadas = [
    (-34.6118, -58.4173),
    (-31.4201, -64.1888),
    (-27.4800, -58.8340),
    (-26.1865, -58.1745),
    (-34.9207, -57.9538),
    (-29.4135, -66.8562),
    (-32.8902, -68.8440),
    (-38.9516, -68.0591),
    (-31.7446, -60.5118),
    (-27.3621, -55.9007),
    (-43.3000, -65.1023),
    (-27.4510, -58.9867),
    (-51.6230, -69.2168),
    (-28.4696, -65.7852),
    (-26.8083, -65.2176),
    (-24.1858, -65.2995),
    (-24.7828, -65.4128),
    (-31.5375, -68.5364),
    (-33.2772, -66.3200),
    (-31.6333, -60.7000),
    (-36.6229, -64.2953),
    (-27.7951, -64.2615),
    (-54.8019, -68.3029),
    (-40.8135, -63.0000),
]

def dibujar_ruta(camino, ciudades, origen=-1):
    # Crear un mapa centrado en una ubicación específica
    latitud = -35.675207
    longitud = -65.423429
    mapa = folium.Map(location=[latitud, longitud], zoom_start=5)

    #Agregar un marcador en cada capital
    for i in range(len(coordenadas)):
        if i != origen:
            folium.Marker(coordenadas[i], tooltip=ciudades[i]).add_to(mapa)

    for i in range(len(camino)-1):
        coords_origen = coordenadas[camino[i]]
        coords_dest = coordenadas[camino[i+1]]
        folium.PolyLine([coords_origen, coords_dest], color="blue", weight=2).add_to(mapa)

    if (origen != -1):
        folium.Marker(coordenadas[origen], tooltip=ciudades[origen], icon=folium.Icon(color='red')).add_to(mapa)

    mapa.save(mapa_path)