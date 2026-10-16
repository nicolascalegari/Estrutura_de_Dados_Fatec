class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(next=head)   
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next