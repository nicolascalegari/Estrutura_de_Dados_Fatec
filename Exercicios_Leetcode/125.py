class Solution:

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Pula caracteres não alfanuméricos à esquerda
            while left < right and not s[left].isalnum():
                left += 1

            # Pula caracteres não alfanuméricos à direita
            while left < right and not s[right].isalnum():
                right -= 1

            # Compara os caracteres convertidos para minúsculo
            if s[left].lower() != s[right].lower():
                return False

            # Move ambos os ponteiros em direção ao centro
            left += 1
            right -= 1

        return True
