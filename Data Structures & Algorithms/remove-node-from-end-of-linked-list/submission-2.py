# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        prev=None
        i=0
        dummy=head
        while dummy:  #finding length 
            i+=1
            dummy=dummy.next
        print(i)
        j=i-n
        i=0
        if j==0:
            return head.next #handles deleting head
        while i<j:
            prev=current
            if current.next:
                current=current.next     #between and deleting end 
            i+=1
        prev.next=current.next
        current=None
        return head
        

