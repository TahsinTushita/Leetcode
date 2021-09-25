class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2) -> ListNode:
        result = ListNode(0)
        h1 = l1
        h2 = l2
        temp = result
        head = None

        while h1 and h2:
            if h1.val >= h2.val:
                if head == None:
                    head = h2
                temp.next = h2
                h2 = h2.next
            else:
                if head == None:
                    head = h1
                temp.next = h1
                h1 = h1.next

            temp = temp.next

        if h1:
            if head == None:
                head = h1
            temp.next = h1
        if  h2:
            if head == None:
                head = h2
            temp.next = h2

        return head

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)

    n1.next = n2
    n2.next = n3

    m1 = ListNode(1)
    m2 = ListNode(3)
    m3 = ListNode(4)

    m1.next = m2
    m2.next = m3

    s1 =Solution()
    head = s1.mergeTwoLists(n1,m1)

    while head:
        print(head.val)
        head = head.next
