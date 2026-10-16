class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        if not nums:
            return 0

        #Ponteiro i marca a posição do ultimo elemento unico encontrado
        i = 0

        #Ponteiro j percorre todo o array procurando novos elementos
        for j in range(1, len(nums)):
            #Se encontrar um elemento diferente do ultimo unico
            if nums[j] != nums[i]:
                i += 1 #Move o ponteiro i para frente
                nums[i] = nums[j] #Copia o elemento unico para posicao i

        #Retorna a qtd de elementos unicos (indice + 1)
        return i + 1


#Ponteiro lento (i): Caminha apenas quando um número inédito é encontrado. 
#Ele reescreve o array eliminando as duplicatas.
#Ponteiro rápido (j): Explora o array elemento por elemento em busca de novidades.
#Lógica de troca: Sempre que nums[j] for diferente de nums[i], significa que 
#passamos pelas duplicatas daquele número. Avançamos i e atualizamos 
#o valor de nums[i] com este novo número.
