class Solution:

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        left = 0
        current_sum = 0
        min_length = float("inf") #Começa com infinito para podermos achar o menor valor

        #O ponteiro 'right' expande a janela
        for right in range(len(nums)):
            current_sum += nums[right]

            #Enquanto a soma for maior ou igual ao target, tentamos encolher a janela pela esquerda
            while current_sum >= target:
                #Calcula o tamanho da janela atual e atualiza o mínimo
                min_length = min(min_length, right - left + 1)

                #Remove o elemento da esquerda e move o ponteiro left para a direita
                current_sum -= nums[left]
                left += 1

        #Se min_length continuou infinito, significa que nenhum subarranjo somou o target
        return min_length if min_length != float("inf") else 0