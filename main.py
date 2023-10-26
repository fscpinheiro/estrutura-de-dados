import itertools

'''
    Permutação
'''
lista = [1,2,3]

for permutacao in itertools.permutations(lista):
    print(permutacao)