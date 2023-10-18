from genetico import N_CIUDADES
import copy

def print_distancias(distancias):
    for ciudad in distancias:
        for dist in ciudad:
            try:
                print("{:4d}".format(dist), end=" ")
            except Exception as e:
                print(dist)
        print("\n")

#Calcula el mejor camino partiendo de una ciudad de origen dado
def metodo_heuristico(origen, distancias):
    cant_visitadas = 0
    dist_total = 0
    camino: list[int] = [origen]
    dist_origen = distancias[origen].copy() #Guardamos las distancias desde el origen para no perderlas

    print_distancias(distancias)
    while cant_visitadas < N_CIUDADES:
        min = int(1e9)
        i = 0
        for dist in distancias[origen]:
            if dist < min and dist != 0:
                min = dist
                index = i
            i += 1

        #Actualizamos los valores de la ciudad ya recorrida
        for i in range(N_CIUDADES+1): 
            distancias[i][origen] = 0 #Columna
            distancias[origen][i] = 0 #Fila 

        camino.append(index)
        origen = index
        dist_total += min
        cant_visitadas += 1
    
    #Volvemos a la ciudad de origen
    dist_total += dist_origen[index]    
    return camino, dist_total

#Calcula el mejor camino con el método heuristico pero no partiendo de una ciudad sino de cualquiera
def heuristico_general(distancias):
    min_dist = 1e9
    min_camino = []

    for ciudad in range(N_CIUDADES):
        camino, dist = metodo_heuristico(ciudad, copy.deepcopy(distancias))
        print("origen:", ciudad)
        print(dist, camino)

        if (dist < min_dist):
            min_dist = dist
            min_camino = camino
        
    return min_camino, min_dist

if __name__ == "__main__":
    metodo_heuristico()