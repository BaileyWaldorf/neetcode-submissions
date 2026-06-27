# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # get halfway point
        slow, fast = head, head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverseList(slow.next)
        slow.next = None

        runner = head
        while runner and second_half:
            tmp1 = runner.next
            runner.next = second_half
            runner = tmp1

            tmp2 = second_half.next
            second_half.next = runner
            second_half = tmp2

    def reverseList(self, head):
        if not head:
            return head
        prev = None
        curr = head
        nxt = head.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt:
                nxt = nxt.next

        return prev
        
        