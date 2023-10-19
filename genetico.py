import random
from util import load_distancias

#----- CONSTANTES ------ #
N_CIUDADES = 24
N_CROMOSOMAS = 50
N_CICLOS = 500
P_CROSSOVER = 0.75
P_MUTACION = 0.1
#----------------------- #

#----- DEFINICIONES ---- #
poblacion = []
#----------------------- #

class Cromosoma:
    genes: list = []
    fitness: float = 0.0
    dist: 0

    def __init__(self):
        #random sample elige N_CIUDADES de una lista=[1..N_CIUDADES] sin repeticion
        self.genes = random.sample(range(0, N_CIUDADES), N_CIUDADES)
        self.genes.append(self.genes[0]) #Agregamos la primer ciudad al final para que vuelva
        self.fitness = 0.0

    #Calcular la distancia total de un recorrido dado
    def set_dist(self, distancias) -> int:
        sum = 0
        for i in range(1, N_CIUDADES-1):
            sum += distancias[self.genes[i]][self.genes[i+1]]
        self.dist = sum

    def set_fitness(self, total: int):  
        self.fitness = (total / self.dist) / N_CROMOSOMAS

    def print_gen(self):
        for value in self.genes:
            print("{:02d}".format(value), end=" ")
        print("\n")

    def test_genes(self, ciclo, nro_cromosoma):
        max = len(self.genes)
        for i in range(max):
            if self.genes[i] in self.genes[i+1:max]:
                print_poblacion()
                print(self.genes)
                print("Gen repetido", self.genes[i], i)
                print("Cromosoma: ", nro_cromosoma)
                print("Ciclo: ", ciclo)
                return False

        return True

#Generar la poblacion inicial
def gen_poblacion():
    for _ in range(N_CROMOSOMAS):
        poblacion.append(Cromosoma())

#Mostrar la poblacion actual
def print_poblacion():
    for cromosoma in poblacion:
        cromosoma.print_gen()

#Mostrar el fitness de todos los cromosomas de la poblacion
def print_fitness():
    i = 0
    for cromosoma in poblacion:
        print(i, cromosoma.fitness, cromosoma.dist)
        i += 1

#Funcion de crossover, cruza dos padres y obtiene dos hijos
#Utilizamos el método de crossover circular
def crossover(padre: Cromosoma, madre: Cromosoma):
    hijo1, hijo2 = Cromosoma(), Cromosoma()
    hijo1.genes = padre.genes.copy()
    hijo2.genes = madre.genes.copy()

    first = padre.genes[0] #Guardar el primer gen del padre
    salto = N_CIUDADES + 1

    i = 0
    while first != salto: #Mientras no volvamos al mismo gen donde empezamos 
        salto = madre.genes[i]
        i = padre.genes.index(salto)

        hijo1.genes[i], hijo2.genes[i] = hijo2.genes[i], hijo1.genes[i]

    return hijo1, hijo2

#Elegimos dos genes al azar e intercambiamos sus valores
def mutacion(cromosoma: Cromosoma):
    indexs = random.sample(cromosoma.genes, 2)
    cromosoma.genes[indexs[0]], cromosoma.genes[indexs[1]] = cromosoma.genes[indexs[1]], cromosoma.genes[indexs[0]]

#Eliminar los cromosomas con peor fitness hasta dejar N_CROMOSOMAS
def borrar_peores():
    global poblacion

    #Ordenar por fitness de modo creciente
    poblacion.sort(key=lambda C: C.dist)

    poblacion = poblacion[:N_CROMOSOMAS]

#Calcular las distancias de cada cromosoma y su funcion fitness
def fitness_poblacion(distancias):
    total = 0
    for cromosoma in poblacion:
        cromosoma.set_dist(distancias)
        total += cromosoma.dist
    for cromosoma in poblacion:
        cromosoma.set_fitness(total)

#Metodo de seleccion, Ruleta con elitismo
def metodo_seleccion():

    #Los dos mejores individuos pasaran directamente a la siguiente generacion
    poblacion.sort(key=lambda C: C.fitness, reverse=True)
    #Ponemos el fitness de los dos mejores individuos en 0 para que no puedan ser seleccionados
    poblacion[N_CROMOSOMAS-1].fitness = 0
    poblacion[N_CROMOSOMAS-2].fitness = 0

    #Seleccionamos N_CROMOSOMAS, los que tengan mejor fitness tendrán más posibilidades de ser seleccionados
    return random.choices(poblacion, [c.fitness for c in poblacion], k = N_CROMOSOMAS)

#
def ciclo(distancias):
    global poblacion

    fitness_poblacion(distancias)
    seleccion = metodo_seleccion()

    for i in range(2, N_CROMOSOMAS, 2):
        #hijos = []

        if random.random() < P_CROSSOVER:
            padre = seleccion[i]
            madre = seleccion[i+1]
            hijo1, hijo2 = crossover(padre, madre)
            #hijos.append(hijo1)
            #hijos.append(hijo2)
            #Los hijos se ponen en lugar de los padre
            poblacion[i] = hijo1
            poblacion[i+1] = hijo2

            if random.random() < P_MUTACION:
                mutacion(poblacion[i])

            if random.random() < P_MUTACION:
                mutacion(poblacion[i+1])

            #Agregamos la primer ciudad al final para hacer que vuelva al origen
            poblacion[i].genes[N_CIUDADES] = poblacion[i].genes[0]
            poblacion[i+1].genes[N_CIUDADES] = poblacion[i+1].genes[0]

        fitness_poblacion(distancias)

def metodo_genetico(distancias):
    gen_poblacion()
    poblacion[0].print_gen()

    i_ciclo = 0
    while i_ciclo < N_CICLOS:
        ciclo(distancias)
        i_ciclo += 1
    print_poblacion()
    print_fitness()
    poblacion[0].print_gen()
    return poblacion[0]

if __name__ == "__main__":
    distancias, ciudades = load_distancias()
    metodo_genetico()