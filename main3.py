def heaps_algorithm(n, lista):
    if n == 1:
        print(lista)
    else:
        for i in range(n - 1):
            heaps_algorithm(n - 1, lista)
            if n % 2 == 0:
                lista[i], lista[n-1] = lista[n-1], lista[i]
            else:
                lista[0], lista[n-1] = lista[n-1], lista[0]
        heaps_algorithm(n - 1, lista)

# Testando
lista = [1,2,3]
heaps_algorithm(len(lista), lista)