# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find the middle
        slow, fast = head, head
        while fast and fast.next: #remember check fast.next isn't None, otherwise python stops the loop before entering
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        second = slow.next #initialize the second half pointer
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge the two halves
        first, second = head, prev #the start of the second half would be prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second #stitch first's arrow to point to second, not second = first.next
            second.next = tmp1 #stitch second's arrow to point to tmp1
            first, second = tmp1, tmp2

