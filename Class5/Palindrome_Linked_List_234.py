class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def isPalindrome(self, head) -> bool:
        list1 = []

        while(head):
            list1.append(head.val)
            head = head.next

        start = 0
        end = len(list1) - 1

        while start < end:
            if list1[start] != list1[end]:
                return False

            start += 1
            end -= 1

        return True

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(2)
    n4 = ListNode(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    s1 = Solution()
    print(s1.isPalindrome(n1))