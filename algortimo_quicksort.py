import random

def gerar_lista(tamanho):
    lista = [random.randint(1, 1000) for _ in range (tamanho)]
    return lista


def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i < pivo]
        maiores = [i for i in lista[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

lista = gerar_lista(200)

print(lista)
print()
print(quicksort(lista))