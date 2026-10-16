class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        anterior = None
        atual = head
        
        while atual:
            
            proximo_no = atual.next # temp
            atual.next = anterior
            anterior = atual
            atual = proximo_no       
            
        return anterior