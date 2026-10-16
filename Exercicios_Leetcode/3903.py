class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            # Maior elemento do inicio ate o indice i
            prefix_max = max(nums[:i+1])

            # Menor elemento do indice i ate o final
            suffix_min = min(nums[i:])

            # Menor ou igual a k, encontrou a resposata
            if prefix_max - suffix_min <= k:
                return i

        return -1