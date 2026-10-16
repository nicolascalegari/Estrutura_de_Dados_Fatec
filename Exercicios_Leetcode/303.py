class NumArray:

    def __init__(self, nums: list[int]):
        #Cria um array de prefixos com um zero extra no inicio
        #Isso facilita o caluclo quando o intervalo começa com indice 0
        self.prefix_sums = [0] * (len(nums) + 1) 

        #Preenche o array com as somas acumuladas
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        #A soma do intervalo L - R é a diferença entre as somas acumuladas
        return self.prefix_sums[right + 1] - self.prefix_sums[left]