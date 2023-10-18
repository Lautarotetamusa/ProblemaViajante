import csv

#Cargar las distancias desde un archivo .csv
#Devuelve la matriz de distancias
#Devuelve el mapa de nombres de las ciudades
def load_distancias(file_path = "TablaCapitales.csv"):
    file_tabla = file_path
    distancias = []

    with open(file_tabla, "r") as tabla:
        reader = csv.reader(tabla);
        header = next(reader)
        ciudades = header[1:len(header)]
        for row in reader:
            first = True
            d = []
            for col in row:
                if not first:
                    if col != "":
                        d.append(int(col))
                    else:
                        d.append(0)
                else:
                    first = False
            distancias.append(d)

    return distancias, ciudades