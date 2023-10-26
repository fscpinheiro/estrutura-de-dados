def permutacoes(lista):
    if len(lista) == 0:
        return []
    elif len(lista) == 1:
        return [lista]
    else:
        l = []
        for i in range(len(lista)):
           m = lista[i]
           remLista = lista[:i] + lista[i+1:]
           for p in permutacoes(remLista):
               l.append([m] + p)
        return l

# Testando a função
lista = [1,2,3]
for p in permutacoes(lista):
    print(p)
