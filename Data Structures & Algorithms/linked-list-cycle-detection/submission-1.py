# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #set two pointers: slow and fast pointers
        #if they met with each other, that means there's a cycle

        slow, fast = head, head

        while fast and fast.next: #make sure the next two steps exist
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
