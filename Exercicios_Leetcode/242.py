class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        #Se tamanhos forem diferentes, nao podem ser anagramas
        if len(s) != len(t):
            return False

        count = {}

        #Incremeta a contagem para letras em 's' e decrementa para 't'
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1

        #Se todas as contagens voltaram para 0, é um anagrama 
        for val in count.values():
            if val != 0:
                return False

        return True
