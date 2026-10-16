class Solution:

    def pivotIndex(self, nums: list[int]) -> int:
        # Soma total de todos os elementos
        total_sum = sum(nums)
        # Começa com zero porque não há elementos à esquerda do índice 0
        left_sum = 0

        for i in range(len(nums)):
            # A soma à direita é o total menos a soma à esquerda menos o próprio elemento atual
            right_sum = total_sum - left_sum - nums[i]
            # Se as somas forem iguais, encontramos o pivô mais à esquerda
            if left_sum == right_sum:
                return i
            # Atualiza a soma à esquerda adicionando o elemento atual antes de passar para o próximo índice
            left_sum += nums[i]

        return -1

