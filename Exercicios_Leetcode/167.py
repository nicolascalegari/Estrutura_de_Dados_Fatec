class Solution:

    def twoSum(self, numbers: list[int], target : int) -> list[int]:

        # Inicializa os dois ponteiros nas extremidades do array
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            #Se encontrou o alvo retorna os indices (baseado em 1)
            if current_sum == target:
                return [left + 1, right + 1]

            #Se a soma for menor move o ponteiro left para a direita
            elif current_sum < target:
                left += 1

            #Se a soma for maior move o ponteiro right para a esquerda
            else:
                right -= 1

        return []

    # Coloca-se um ponteiro no inicio left e outro no fim right do array
    # Calcula-se a soma dos dois elementos apontados
    # Se current_sum == target Algoritimo encerrado
    # Se current_sum < target a soma precisa aumentar. Como o array esta ordenado,
    # move-se o ponteiro left para a direita
    # Se current_sum > target a soma precisa diminuir. Move-se o ponteiro right
    # para a esquerda.
    # Tempo O(n)
    # Espaço O(1)