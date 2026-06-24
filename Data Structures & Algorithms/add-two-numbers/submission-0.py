# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current=l1
        num=""
        while current:
            str1=str(current.val)
            num+=str1
            print(num)
            current=current.next
        num=int(num[::-1])
        current=l2
        num1=""
        while current:
            str1=str(current.val)
            num1+=str1
            current=current.next
        num1=int(num1[::-1])
        res=num1+num
        res=str(res)[::-1]
        h = ListNode(int(res[0]))
        result = h

        for char in res[1:]:
            result.next = ListNode(int(char))
            result = result.next

        return h


        