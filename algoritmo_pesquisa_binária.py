# Função para criar uma lista com varios numeros 
def createList(n):
    lst = []
    for i in range(n + 1):
        lst.append(i)
    return lst

# Algoritmo
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) -1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        if chute < item:
            baixo = meio + 1
    return None

lista = createList(1000)
lista = sorted(lista)

print(pesquisa_binaria(lista, 250))