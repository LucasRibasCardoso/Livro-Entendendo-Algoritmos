# Exemplo de implementação de pesquisa em largura

from collections import deque

def pessoa_e_vendedor(pessoa):
    return pessoa[-1] == 'm'


grafo = {}
grafo["Lucas"] = ["Anna", "Guilherme", "Maria"]
grafo["Anna"] = []
grafo["Guilherme"] = ["Rodolfo"]
grafo["Rodolfo"] = []
grafo["Maria"] = ["Maincom"]

def pesquisa(nome):
    fila_pesquisa = deque()
    fila_pesquisa += grafo[nome]
    pessoas_verificadas = []

    while fila_pesquisa:
        pessoa = fila_pesquisa.popleft()
        if pessoa not in pessoas_verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de manga!")
            else:
                
                fila_pesquisa += grafo[pessoa]
                pessoas_verificadas.append(pessoa)
    return False

pesquisa("Lucas")