from genetico import Cromosoma, crossover

def test_crossver():
    padre = Cromosoma()
    padre.genes = [6, 9, 18, 2, 15, 5, 3, 4, 0, 10, 20, 11, 22, 17, 12, 13, 8, 16, 7, 19, 1, 14, 21]
    #N_CIUDADES = 10
    #padre.genes = [9, 8, 2, 0, 7, 4, 5, 1, 6, 3]

    madre = Cromosoma()
    madre.genes = [0, 1, 18, 21, 6, 16, 7, 5, 12, 19, 2, 9, 22, 20, 8, 4, 3, 17, 15, 11, 13, 10, 14]
    #madre.genes = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1]

    print("Padres")
    padre.print_gen()
    madre.print_gen()
    hijo1, hijo2 = crossover(padre, madre)
    print("Hijos")
    hijo1.print_gen()
    hijo2.print_gen()

    good1 = hijo1.test_genes(0, 0)
    good2 = hijo2.test_genes(0, 1)

    assert(good1 and good2)

if __name__ == "__main__":
    test_crossver()