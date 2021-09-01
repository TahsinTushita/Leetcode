class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head) -> ListNode:
        stack = []
        while(head):
            stack.append(head)
            head = head.next

        new_head = None
        prev = None

        while(stack):
            temp = stack.pop()

            if new_head == None:
                new_head = temp
                prev = temp
            else:
                prev.next = temp
                prev = temp

        if(prev):
            prev.next = None

        return new_head

if __name__ == '__main__':
    h1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    h1.next = n2
    n2.next = n3

    s1 = Solution()
    head = s1.reverseList(h1)

    while(head):
        print(head.val)
        head = head.next