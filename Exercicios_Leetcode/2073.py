class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        tempo_total = 0
        tickets_k = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                tempo_total += min(tickets[i], tickets_k)
            else:
                tempo_total += min(tickets[i], tickets_k - 1)

        return tempo_total
    
        