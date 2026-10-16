class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Guarda o último índice de cada caractere
        left = 0  # Ponteiro da esquerda (início da janela)
        max_length = 0  # Guarda o maior comprimento encontrado

        # O ponteiro 'right' expande a janela caractere por caractere
        for right in range(len(s)):
            current_char = s[right]

            # Se o caractere já foi visto E está dentro da janela atual
            if current_char in char_index and char_index[current_char] >= left:
                # Move o ponteiro 'left' para logo após a última aparição do caractere
                left = char_index[current_char] + 1

            # Atualiza o índice do caractere atual para a posição mais recente
            char_index[current_char] = right

            # Calcula o tamanho da janela atual e atualiza o máximo
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length

        return max_length