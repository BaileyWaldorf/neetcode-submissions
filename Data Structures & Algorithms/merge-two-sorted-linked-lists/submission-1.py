# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        runner = new_head

        while list1 and list2:
            if list1.val < list2.val:
                runner.next = list1
                list1 = list1.next
            else:
                runner.next = list2
                list2 = list2.next

            runner = runner.next
        
        # append the rest if there are any remaining items in either list (they must be larger since it's sorted)
        runner.next = list1 or list2

        return new_head.next