# Trabajo Práctico Algoritmos Geneticos

### Ingeniería en Sistemas de Información UTN Rosario

### Integrantes:

- Lautaro Teta Musa
- Rodrigo Mari
- Marcos del Solar

## Enunciado

#### El problema del Viajante

El problema del viajante (también conocido como problema del viajante de comercio o por sus siglas en inglés: TSP
(Traveling Salesman Problem), es uno de los problemas más famosos (y quizás el mejor estudiado) en el campo de la optimización combinatoria computacional.

A pesar de la aparente sencillez de su planteamiento, el TSP es uno de los más complejos de resolver .

**Definición:**

Sean N ciudades de un territorio. La distancia entre cada ciudad viene dada por la matriz D: NxN,
donde d[x,y] representa la distancia que hay entre la ciudad X y la ciudad Y.

El **objetivo** es encontrar una ruta que, comenzandoy terminando en una ciudad concreta,pase una sola vez por cada una de las ciudades y minimice la distancia recorrida por el viajante.

**Ejercicios:**

1. **Hallar
   la ruta de distancia mínim**a que logre unir todas las capitales de provincias de
   la República Argentina, utilizando un método exhaustivo.
   ¿Puede resolver el problema? Justificar de manera teórica.
2. **Realizar
   un programa** que cuente con un menú con las siguientes opciones:

a) Permitir ingresar una provincia y hallar la ruta de distancia mínima que logre unir todas las capitales de
provincias de la República Argentina partiendo de dicha capital utilizando la siguiente heurística: **“Desde cada ciudad ir a la ciudad más cercana no visitada.**”
**Recordar regresar siempre a la ciudad de partida**.

Presentar un mapa de la República con el recorrido indicado. Además indicar la ciudad de partida, el recorrido
completo y la longitud del trayecto. El programa deberá permitir seleccionar la capital que el usuario desee ingresar como inicio del recorrido.

b) **Encontrar el recorrido mínimo** para visitar todas las capitales de las provincias de la República Argentina siguiendo la heurística mencionada en el punto a. Deberá mostrar como salida el recorrido y la longitud del trayecto.

c) **Hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina, utilizando un algoritmo genético** .


## Modo de Uso

### Instalacion

Clonar el repositorio

```
git clone https://github.com/Lautarotetamusa/ProblemaViajante.git
```

Si queremos instalar las librerías necesesarias en un entorno que no se queden guardadas en nuestra máquina

```
python -m venv -venv
source .venv/bin/activate
```

instalar las librerías necesarias

```
pip install -r requeriments.txt
```

### Uso

python main.py `<Method>`

METHODS:
  	'heuristico origen'  Método Heuristico partiendo desde una ciudad
  	'heuristico general' Método Heuristico general
  	'genetico' Método Genetico \
