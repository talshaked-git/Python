# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    ptr1, ptr2 = l1, l2
    carry = 0
    
    while ptr1 or ptr2:
        x = ptr1.val if ptr1 else 0
        y = ptr2.val if ptr2 else 0
        total = x + y + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if ptr1: ptr1 = ptr1.next
        if ptr2: ptr2 = ptr2.next
    
    if carry > 0:
        current.next = ListNode(carry)
    
    return dummy_head.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1,l2)

while result:
    print(result.val, end=" ")
    result = result.next