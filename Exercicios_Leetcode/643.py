class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        #Calcula a soma da primeira janela de tamanho k
        current_sum = sum(nums[:k])
        max_sum = current_sum

        #Desliza a janela pelo restante do array
        for i in range(k, len(nums)):
            #Adiciona o proximo elemento e remove o primeiro da janela anterior
            current_sum += nums[i] - nums[i - k]

            #Atualiza a maior soma encontrada
            if current_sum > max_sum:
                max_sum = current_sum

        #Retorna a maior media
        return max_sum / k