class Solution:
    def reverseString(self , s: list[str]) -> None:
        #Inicia um ponteiro no comeco e outro no fim do array
        left = 0
        right = len(s) - 1

        #Enquanto os ponteiros nao se cruzam
        while left < right:
            #Troca os caracteres de posicao
            s[left], s[right] = s[right], s[left]

            #Move o ponteiro em direção ao centro
            left += 1
            right -= 1