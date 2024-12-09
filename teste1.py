from typing import List, Tuple


def defini_posicao(x: list[str]) -> List[Tuple]:
    len_max = 78
    
    linhas = []
    for i in range(len(x)):
        palavras = x[i].split()  # Divide a string em palavras
        linha_atual = ""
    
        for palavra in palavras:
            # Verifica se adicionar a próxima palavra excede o tamanho máximo
            if len(linha_atual) + len(palavra) + 1 <= len_max:
                linha_atual += (palavra + " ")  # Adiciona a palavra à linha atual
            else:
                linhas.append((linha_atual.strip(), (len(linhas)+1)*30))  # Adiciona a linha à lista de linhas
                linha_atual = palavra + " "  # Começa uma nova linha com a palavra atual

        if linha_atual:  # Adiciona a última linha, se existir
            linhas.append((linha_atual.strip(), (len(linhas)+1)*30))
    
    return linhas

text = ["dfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgs",
        "dfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgs",
        "dfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgs",
        "dfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgsdfgsdf sfg esgf rdzhhzdrhdr rd rzdtgdzg rzgzrdg rz gzrd rgzzrg rzrzgzsegegdf rsgt estz erssdfds rsg rsgsg sesegsdgs"
        ]
print(defini_posicao(text))
