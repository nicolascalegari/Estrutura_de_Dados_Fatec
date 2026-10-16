import random


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n  # Total de elementos na matriz
        self.dicionario = (
            {}
        )  # Mapeamento virtual para o algoritmo de Fisher-Yates
        self.zeros_restantes = self.total

    def flip(self) -> list[int]:
        # Escolhe um índice virtual aleatório dentro do escopo de zeros restantes
        idx_sorteado = random.randint(0, self.zeros_restantes - 1)

        # Se o índice sorteado já foi mapeado, pega o valor real. Caso contrário, usa ele mesmo.
        valor_real = self.dicionario.get(idx_sorteado, idx_sorteado)

        # O índice sorteado agora deve apontar para o valor armazenado na "última posição disponível"
        ultima_posicao = self.zeros_restantes - 1
        self.dicionario[idx_sorteado] = self.dicionario.get(
            ultima_posicao, ultima_posicao
        )

        # Reduz a quantidade de zeros disponíveis para a próxima chamada
        self.zeros_restantes -= 1

        # Converte o valor em coordenadas da matriz (linha, coluna)
        linha = valor_real // self.n
        coluna = valor_real % self.n

        return [linha, coluna]

    def reset(self) -> None:
        # Limpa o dicionário e reseta o contador de elementos
        self.dicionario.clear()
        self.zeros_restantes = self.total
