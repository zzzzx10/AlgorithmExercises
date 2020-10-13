# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return ListNode(-1)
        pre = head
        while pre != slow:
            pre = pre.next
            slow = slow.next
        return pre


n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(0)
n4 = ListNode(-4)
n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n2
s = Solution()

m1 = ListNode(0)
print(s.detectCycle(n1).val)
print(s.detectCycle(m1).val)
