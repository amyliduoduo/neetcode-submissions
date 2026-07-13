# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #set slow and fast pointer to find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half of the linked list
        second = slow.next #start of second half of the list
        slow.next = None #disconnects the first half from the seond half so they don't accidentally form a loop
        prev = None
        while second:
            tmp = second.next
            second.next = prev #flip the arrow to reverse
            prev = second #move prev forward
            second = tmp #move second forward
        
        #merging the two halves together
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



        