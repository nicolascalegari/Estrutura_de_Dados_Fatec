class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Inicializa ambos os ponteiros no início da lista
        slow = head
        fast = head
        
        # O ponteiro rápido avança de 2 em 2, então precisamos garantir
        # que ele e o próximo nó existam para evitar erros de NoneType
        while fast and fast.next:
            slow = slow.next          # Anda 1 passo
            fast = fast.next.next     # Anda 2 passos
            
            # Se os ponteiros se encontrarem, significa que há um ciclo
            if slow == fast:
                return True
                
        # Se o ponteiro rápido chegar ao final da lista (None), não há ciclo
        return False
