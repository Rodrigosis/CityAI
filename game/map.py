import random


class Estrutura:
    def __init__(self, id=None, nome=None, cima=None, baixo=None, esquerda=None, direita=None):
        """
        Representa um ponto do mapa com seus atributos.
        :param id: int - Identificador único da estrutura.
        :param nome: str - Nome da estrutura.
        :param cima, baixo, esquerda, direita: int ou None - IDs das conexões na matriz.
        """
        self.id = id
        self.nome = nome
        self.cima = cima
        self.baixo = baixo
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        """
        Representação de cada objeto como string para depuração.
        """
        return f"{self.nome}(ID={self.id})(cima={self.cima},baixo={self.baixo},esquerda={self.esquerda},direita={self.direita})"


def find_local(map, local_id: int):
    local = None
    for linha in map:
        for ponto in linha:
            if int(ponto.id) == local_id:
                local = ponto
                break
        if local:
            break
    return local

def create_mini_map(map, local_id_centro):
    def get_position(local, direction):
        """Função auxiliar para encontrar uma posição no mapa, se for válida."""
        return find_local(map, getattr(local, direction)) if local and getattr(local, direction, None) else None

    # Inicializa uma grade 7x7 com None (representando os 49 locais)
    mini_map = [[None for _ in range(7)] for _ in range(7)]

    # Define o centro do mapa (posição 3,3 na matriz 7x7)
    pos_24 = find_local(map, local_id_centro)
    mini_map[3][3] = pos_24

    # Preenche horizontalmente em torno do centro (linha central)
    for offset in range(1, 4):
        mini_map[3][3 + offset] = get_position(mini_map[3][3 + offset - 1], "direita")  # À direita
        mini_map[3][3 - offset] = get_position(mini_map[3][3 - offset + 1], "esquerda")  # À esquerda

    # Preenche verticalmente em torno da linha central (para cima e para baixo)
    for row in range(2, -1, -1):  # Para cima (linhas acima do centro)
        for col in range(7):
            mini_map[row][col] = get_position(mini_map[row + 1][col], "cima")

    for row in range(4, 7):  # Para baixo (linhas abaixo do centro)
        for col in range(7):
            mini_map[row][col] = get_position(mini_map[row - 1][col], "baixo")

    return [mini_map[row][col] for row in range(7) for col in range(7)]


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


def gerar_mapa(largura_altura: int):
    """
    Gera um mapa aleatório contendo várias estruturas interligadas por ruas.
    Cada estrutura está conectada a uma rua e todas as ruas estão interligadas.
    :param largura_altura: int - Quantidade de colunas e linha no mapa.
    :return: list - Lista de objetos Estrutura formando o mapa e os NPCs posicionados.
    """
    tipos_estruturas = [
        "casa", "mansão", "prédio residencial", "office", "hospital", "park",
        "shopping", "delegacia", "praia", "prisão", "academia", "fábrica",
        "escola", "igreja", "bar", "bordel", "porto", "fazenda"
    ]

    mapa = []
    id_counter = 0

    # Gera os pontos do mapa de forma aleatória
    for y in range(largura_altura):
        linha = []
        for x in range(largura_altura):
            tipo_estrutura = "rua" if random.random() < 0.4 else random.choice(
                tipos_estruturas)  # 40% de chance de ser rua
            ponto = Estrutura(
                id=id_counter,
                nome=tipo_estrutura,
                cima=None,
                baixo=None,
                esquerda=None,
                direita=None
            )
            linha.append(ponto)
            id_counter += 1
        mapa.append(linha)

    # # Garantir que todas as ruas estão conectadas
    # for y in range(largura_altura):
    #     for x in range(largura_altura):
    #         ponto_atual = mapa[y][x]
    #
    #         # Se for uma estrutura e não houver ruas próximas, cria uma conexão com uma rua
    #         if ponto_atual.nome != "rua":
    #             vizinhos = []
    #             if y > 0:
    #                 vizinhos.append(mapa[y - 1][x])  # cima
    #             if y < largura_altura - 1:
    #                 vizinhos.append(mapa[y + 1][x])  # baixo
    #             if x > 0:
    #                 vizinhos.append(mapa[y][x - 1])  # esquerda
    #             if x < largura_altura - 1:
    #                 vizinhos.append(mapa[y][x + 1])  # direita
    #
    #             # Garante que cada estrutura está ligada a pelo menos uma rua
    #             if all(vizinho.nome != "rua" for vizinho in vizinhos):
    #                 random.choice(vizinhos).nome = "rua"

    # Conecta os IDs vizinhos
    for y in range(largura_altura):
        for x in range(largura_altura):
            ponto_atual = mapa[y][x]
            if y > 0:
                ponto_atual.cima = mapa[y - 1][x].id
            if y < largura_altura - 1:
                ponto_atual.baixo = mapa[y + 1][x].id
            if x > 0:
                ponto_atual.esquerda = mapa[y][x - 1].id
            if x < largura_altura - 1:
                ponto_atual.direita = mapa[y][x + 1].id

    # id_count = 0
    # for a in range(largura_altura):
    #     for b in range(largura_altura):
    #         pos = calcular_vizinhos(largura_altura, a, b)
    #         mapa[a][b].id = id_count
    #         mapa[a][b].cima = pos["cima"]
    #         mapa[a][b].baixo = pos["baixo"]
    #         mapa[a][b].esquerda = pos["esquerda"]
    #         mapa[a][b].direita = pos["direita"]
    #         id_count += 1
    return mapa


def salvar_mapa_html(mapa, arquivo="mapa.html"):
    """
    Gera e salva um arquivo HTML que mostra o mapa.
    :param mapa: list - Mapa 2D gerado pelo algoritmo.
    :param arquivo: str - Nome do arquivo HTML gerado.
    """
    # CSS para visualização
    estilo_css = """
    <style>
        .outer-box {
            display: grid;
            grid-template-columns: repeat(AUTOMATICO, 1fr);
            gap: 5px;
            padding: 10px;
            background-color: #f9f9f9;
            border: 2px solid #ccc;
            border-radius: 10px;
            width: fit-content;
            margin: 20px auto;
        }
        .inner-box {
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            width: 80px;
            height: 80px;
            background-color: #4287f5;
            color: white;
            font-weight: bold;
            text-align: center;
        }
        .rua {
            background-color: #686868;
        }
    </style>
    """
    # Corpo HTML baseado no mapa
    html = ["<div class='outer-box'>"]
    for linha in mapa:
        for ponto in linha:
            classes = "inner-box"
            if ponto.nome == "rua":
                classes += " rua"
            html.append(f"<div class='{classes}'>{ponto.nome} (ID={ponto.id})</div>")
    html.append("</div>")

    # Ajuste da largura na grade
    largura_css = estilo_css.replace("AUTOMATICO", str(len(mapa[0])))
    conteudo_html = f"<!DOCTYPE html><html><head>{largura_css}</head><body>{''.join(html)}</body></html>"

    # Salva o HTML em um arquivo
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo_html)


if __name__ == "__main__":
    # Configurações do mapa
    largura_altura = 15  # Largura e Altura do mapa (colunas)

    # Gerar o mapa
    mapa_gerado = gerar_mapa(largura_altura)

    for i in mapa_gerado:
        print(i)

    # Salvar o mapa em um arquivo HTML
    salvar_mapa_html(mapa_gerado, "mapa.html")

    from game.player import NewPlayer
    player = NewPlayer()
    mini_map = create_mini_map(mapa_gerado, player.local_id)
