from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #Cria um dicionario onde o valor padrao de qualquer chave nova é um lista vazia
        anagrams_map = defaultdict(list)

        for s in strs:
            # Ordena as letras da string. Ex: "eat" vira ['a', 'e', 't']
            # O join transforma de volta em string: "aet"
            sorted_str = "".join(sorted(s))
            # Agrupa a string original usando a versão ordenada como chave
            anagrams_map[sorted_str].append(s)
        # Retorna apenas as listas agrupadas do dicionário
        return list(anagrams_map.values())