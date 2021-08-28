class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2) -> ListNode:
        list1 = []
        list2 = []

        while(l1):
            list1.append(l1.val)
            l1 = l1.next

        while (l2):
            list2.append(l2.val)
            l2 = l2.next

        reverseList1 = []
        while(list1):
            reverseList1.append(list1.pop())

        reverseList2 = []
        while (list2):
            reverseList2.append(list2.pop())

        strDigitList1 = [str(digit) for digit in reverseList1]
        strDigits1 = "".join(strDigitList1)
        intDigits1 = int(strDigits1)

        strDigitList2 = [str(digit) for digit in reverseList2]
        strDigits2 = "".join(strDigitList2)
        intDigits2 = int(strDigits2)

        intResult = intDigits1 + intDigits2
        strDigits = str(intResult)
        listResult = [int(digit) for digit in strDigits]

        head = None
        prev = None
        while(listResult):
            new_node = ListNode(listResult.pop())

            if head == None:
                head = new_node
                prev = new_node
            else:
                prev.next = new_node
                prev = prev.next

        return head

if __name__ == '__main__':
    h1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)

    h1.next = n2
    n2.next = n3

    h2 = ListNode(5)
    n2 = ListNode(6)
    n3 = ListNode(4)

    h2.next = n2
    n2.next = n3

    s1 = Solution()
    head = s1.addTwoNumbers(h1,h2)
    while(head):
        print(head.val)
        head = head.next