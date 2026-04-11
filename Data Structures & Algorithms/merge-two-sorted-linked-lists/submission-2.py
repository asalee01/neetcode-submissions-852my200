# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        mergedHead = ListNode()
        #covers non-existent cases
        if (not list1 or not list2):
            if (not list1 and not list2):
                return None
            elif (not list1):
                return list2
            else:
                return list1
        

        curr1, curr2 = list1, list2
        if (curr1.val < curr2.val):
            merged, mergedHead = curr1, curr1
            curr1 = curr1.next
        else:
            merged, mergedHead = curr2, curr2
            curr2 =curr2.next
        while(curr1 and curr2):
            if (curr1.val < curr2.val):
                merged.next = curr1
                curr1 = curr1.next
            else:
                merged.next = curr2
                curr2 = curr2.next
            merged = merged.next
        if (not curr2):
            merged.next = curr1
        else:
            merged.next = curr2
        return mergedHead    
        

        


        