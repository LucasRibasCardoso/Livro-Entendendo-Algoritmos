def contar(lista):
    if lista == []:
        return 0
    else:
        return 1 + contar(lista[1:])



print(contar([1,2,3]))