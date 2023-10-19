from genetico import metodo_genetico, N_CIUDADES, N_CICLOS
from draw_map import dibujar_ruta
from heuristica import metodo_heuristico, heuristico_general
from util import load_distancias
import sys
import os

#distancias: list[list[int]] = []

def usage():
    print("----------- USAGE ------------")
    print("python main.py <Method>\n")
    print("METHODS: ")
    print("   'heuristico origen'  Método Heuristico partiendo desde una ciudad")
    print("   'heuristico general' Método Heuristico general")
    print("   'genetico' Método Genetico")

commands = {
    "heuristico origen": metodo_heuristico,
    "heuristico general": "TODO",
    "genetico": metodo_genetico,
}

if __name__ == "__main__":
    if (len(sys.argv) > len(commands) or len(sys.argv) < 2):
        usage()
        exit(1)
    else:
        #Almacenamos la matriz de distancias y los nombres de las ciudades
        distancias, ciudades = load_distancias()

        if (sys.argv[1] == "heuristico"):
            if (sys.argv[2] == "origen"):
                origen = int(input("Ingrese una ciudad: "))
                while (origen <= 0 or origen > N_CIUDADES):
                    origen = int(input("La ciudad ingresada no existe, ingrese otra: "))

                camino, dist = metodo_heuristico(origen, distancias)
            
            elif (sys.argv[2] == "general"): 
                camino, dist = heuristico_general(distancias)
                origen = camino[0]

            else:
                print(" Opcion Incorrecta ")
                usage()
                exit(1)

        elif (sys.argv[1] == "genetico"):
            cromosoma = metodo_genetico(distancias)
            camino = cromosoma.genes
            dist = cromosoma.dist
            origen = -1

        else:
            print(" Opcion Incorrecta ")
            usage()
            exit(1)

        dibujar_ruta(camino, ciudades, origen)
        for ciudad in camino:
            print(ciudades[ciudad])
        print("Generacion terminada.")
        print("Mapa de rutas generado en")
        print(f"file://{os.getcwd()}/ruta.html")
        print("Cantidad de iteraciones: ", N_CICLOS)
        print("Distancia minima: ", dist)            