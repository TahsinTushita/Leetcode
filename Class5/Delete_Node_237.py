class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(1)
    n4 = ListNode(9)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    s1 = Solution()
    s1.deleteNode(n2)

    while(n1):
        print(n1.val)
        n1 = n1.next