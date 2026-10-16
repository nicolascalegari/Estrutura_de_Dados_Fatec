class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        # Conjunto de vogais para busca rápida O(1)
        vowels = {"a", "e", "i", "o", "u"}

        # 1. Conta as vogais da primeira janela de tamanho k
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # 2. Desliza a janela pelo restante da string
        for i in range(k, len(s)):
            # Se o caractere que entra for vogal, incrementa
            if s[i] in vowels:
                current_vowels += 1
            # Se o caractere que sai era vogal, decrementa
            if s[i - k] in vowels:
                current_vowels -= 1

            # Atualiza o máximo encontrado
            if current_vowels > max_vowels:
                max_vowels = current_vowels

            # Otimização: se já encontramos o máximo possível (k), podemos parar
            if max_vowels == k:
                return k

        return max_vowels