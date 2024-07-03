from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def obtener_ubicacion(ciudad):
    geolocalizador = Nominatim(user_agent="calculadora_distancia")
    ubicacion = geolocalizador.geocode(ciudad)
    return (ubicacion.latitude, ubicacion.longitude)

def calcular_distancia(origen, destino):
    coords_origen = obtener_ubicacion(origen)
    coords_destino = obtener_ubicacion(destino)
    km = geodesic(coords_origen, coords_destino).kilometers
    millas = geodesic(coords_origen, coords_destino).miles
    return km, millas

def viaje(horas):
    minutos = int(horas * 60)
    horas = minutos // 60
    minutos = minutos % 60
    return horas, minutos

def main():
    while True:
        print("Para salir, ingrese 's'")
        origen = input("Ingrese la Ciudad de Origen: ")
        if origen.lower() == 's':
            break
        destino = input("Ingrese la Ciudad de Destino: ")
        if destino.lower() == 's':
            break

        km, millas = calcular_distancia(origen, destino)
        print(f"Distancia desde {origen} hasta {destino}:")
        print(f"{km:.2f} kilómetros")
        print(f"{millas:.2f} millas")

        modos_transporte = {
            "1": ("auto", 80),
            "2": ("Transporte Público", 50),
            "3": ("Para viajes largos - Avión", 900),
            "4": ("Para viajes largos - Barco", 40),
            "5": ("Para viajes largos - Tren", 120)
        }

        print("Seleccione el medio de transporte:")
        print("1. auto (80 km/h)")
        print("2. Transporte Público (50 km/h)")
        print("3. Para viajes largos - Avión (900 km/h)")
        print("4. Para viajes largos - Barco (40 km/h)")
        print("5. Para viajes largos - Tren (120 km/h)")
        eleccion = input("Ingrese el número correspondiente al medio de transporte: ")

        if eleccion in modos_transporte:
            modo, velocidad = modos_transporte[eleccion]
            horas = km / velocidad
            horas, minutos = viaje(horas)
            print(f"Duración estimada del viaje en {modo}: {horas} horas y {minutos} minutos")

if __name__ == "__main__":
    main()
