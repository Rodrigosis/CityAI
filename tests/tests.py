# Criar uma matriz 15x15 com números de 0 a 49 aleatórios
import random


def calcular_vizinhos(tamanho_matriz: int, x: int, y: int):
    """
    Calcula os números das posições vizinhas (acima, abaixo, à esquerda e à direita)
    de um elemento na matriz.
    :param tamanho_matriz: int - Tamanho da matriz. Ex.: 15 para uma matriz 15x15.
    :param x: int - Índice da coluna (posição horizontal).
    :param y: int - Índice da linha (posição vertical).
    :return: dict - Números dos vizinhos {'cima': ..., 'baixo': ..., 'esquerda': ..., 'direita': ...}.
    """
    assert tamanho_matriz > x
    assert tamanho_matriz > y

    matriz = []  # Inicializa a matriz vazia

    numero = 0  # Número inicial
    for i in range(tamanho_matriz):
        linha = []  # Inicializa uma nova linha
        for j in range(tamanho_matriz):
            linha.append(numero)  # Adiciona o número atual à linha
            numero += 1  # Incrementa o número
        matriz.append(linha)  # Adiciona a linha à matriz


    numero_vizinhos = {"cima": None, "baixo": None, "esquerda": None, "direita": None}

    # Verifica acima
    if y > 0:  # Somente se não estiver na primeira linha
        numero_vizinhos["cima"] = matriz[y - 1][x]

    # Verifica abaixo
    if y < len(matriz) - 1:  # Somente se não estiver na última linha
        numero_vizinhos["baixo"] = matriz[y + 1][x]

    # Verifica à esquerda
    if x > 0:  # Somente se não estiver na primeira coluna
        numero_vizinhos["esquerda"] = matriz[y][x - 1]

    # Verifica à direita
    if x < len(matriz[0]) - 1:  # Somente se não estiver na última coluna
        numero_vizinhos["direita"] = matriz[y][x + 1]

    return numero_vizinhos


if __name__ == "__main__":

    # Teste com um índice específico, por exemplo (7, 7)
    x = 0  # Coluna
    y = 0  # Linha
    vizinhos = calcular_vizinhos(15, 2, 0)

    print(vizinhos)
