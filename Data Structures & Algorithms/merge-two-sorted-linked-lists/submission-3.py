# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #compare the values from each list each time

        #for empty merged list,set two pointers: dummy and tail
        dummy = tail = ListNode()

        while list1 and list2: #"list1" and "list2" are pointers (provided by python), they are not the whole lists
            if list1.val <= list2.val: #comparing the value "list1.val" not just "list1"
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        #edge case: if one of the list is empty
        tail.next = list1 or list2
        

        return dummy.next

 