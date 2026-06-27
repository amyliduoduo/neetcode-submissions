# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #Dummy node: creates a brand-new, empty linked list node in memory and points two different variables (dummy and node) to that exact same node.
        #so that we don't need to worry about whether list 1 or list 2 has the smaller first number
        #just directly attach everything to the back of this dummy node without worrying about edge cases.
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2

        return dummy.next


        