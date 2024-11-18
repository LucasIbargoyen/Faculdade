import random

"""
Função lógica do campo minado, basicamente essa função monta o tabuleiro do campo minado, essa função também
cria as minas no campo, separando elas pelas colunas e fileiras
""" 
def criarCampoMinado(fileira, colunas, numeroMinas):
    campoMinado = [[0 for _ in range(colunas)] for _ in range(fileira)]
    minas = random.sample(range(fileira * colunas), numeroMinas)
    for mina in minas:
        r, c = divmod(mina, colunas)
        campoMinado[r][c] = -1

    for r in range(fileira):
        for c in range(colunas):
            if campoMinado[r][c] == -1:
                continue
            campoMinado[r][c] = sum(
                campoMinado[i][j] == -1
                for i in range(max(0, r-1), min(fileira, r+2))
                for j in range(max(0, c-1), min(colunas, c+2))
            )
    return campoMinado

# Essa função mostra as interações no campo minado, se o usuário clicou numa bomba ou não
def mostrarCampoMinado(campoMinado):
    for row in campoMinado:
        print(" ".join(str(cell) if cell != -1 else "*" for cell in row))

# Como dito anteriormente, essa função serve para a movimentação dos blocos, se eles são minados ou não
def fazer_movimento(campo_minado, fileira, coluna):
    if campo_minado[fileira][coluna] == -1:
        return "Game Over"
    return campo_minado[fileira][coluna]
