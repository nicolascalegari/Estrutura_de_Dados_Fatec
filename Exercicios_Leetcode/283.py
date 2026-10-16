class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        #Ponteiro i marca a posição onde o proximo numero diferente de 0 deve ir
        i = 0

        #Ponteiro j percorre todo o array
        for j in range(len(nums)):
            #Se encontrar um numero que nao e zero
            if nums[j] != 0:
                #Troca os elementos de lugar
                nums[i], nums[j] = nums[j], nums[i]
                #Avança o ponteiro i
                i += 1

#Ponteiro i (lento) Aponta para a posição do primeiro zero encontrado ou para o
#espaço onde o próximo número diferente de zero deve ser posicionado.
#Ponteiro j (rapido) Explora o array elemento por elemento.
#Quando nums[j] encontra um número que não é zero, ele troca 
#de lugar com nums[i]. Isso empurra os zeros para a direita e traz os números 
#normais para a esquerda, mantendo a ordem deles.