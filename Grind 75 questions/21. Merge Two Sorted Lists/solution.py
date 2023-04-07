# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        if temp1 != None and temp2 != None:
            if temp1.val <= temp2.val:
                root = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                root = ListNode(temp2.val)
                temp2 = temp2.next
        elif temp1 == None:
            return temp2
        elif temp2 == None:
            return temp1
        prev = root
        while temp1 != None and temp2 != None:
            if temp1.val <= temp2.val:
                curr = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                curr = ListNode(temp2.val)
                temp2 = temp2.next
            prev.next = curr
            prev = curr
        if temp1 == None:
            while temp2 != None:
                curr = ListNode(temp2.val)
                temp2 = temp2.next
                prev.next = curr
                prev = curr
        elif temp2 == None:
            while temp1 != None:
                curr = ListNode(temp1.val)
                temp1 = temp1.next
                prev.next = curr
                prev = curr
        return root
