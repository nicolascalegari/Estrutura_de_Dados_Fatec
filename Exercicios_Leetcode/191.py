class Solution:
    def hammingWeight(self, n: int) -> int:
        contador = 0

        while n > 0:

            # Remove o bit 1 mais a direita
            n = n & (n - 1)

            contador += 1

        return contador