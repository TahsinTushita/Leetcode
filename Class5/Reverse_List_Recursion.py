class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseListRecursively(self, head) -> ListNode:
        if head == None:
            return head
        if head.next == None:
            return head

        node = self.reverseListRecursively(head.next)
        head.next.next = head
        head.next = None
        return node

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    n1.next = n2
    n2.next = n3

    s1 = Solution()
    head = s1.reverseListRecursively(n1)

    while(head):
        print(head.val)
        head = head.next
