def mais_alto(lista):
    if len(lista) == 2:
        return list[0] if lista[0] > lista[1] else lista[1]
    else:
        sub_max = mais_alto(lista[1:])
        return lista[0] if lista[0] > sub_max else sub_max


print(mais_alto([1,2,3,10,5]))