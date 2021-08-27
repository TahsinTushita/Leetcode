class Node:
    def __int__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0)

    def addAtHead(self,val):
        self.addAtIndex(0,val)

    def addAtTail(self,val):
        self.addAtIndex(self.size,val)

    def addAtIndex(self,index,val):
        if index > self.size:
            return

        self.size += 1

        temp = self.head

        for _ in range(index):
            temp = temp.next

        new_node = Node(val)
        new_node.next = temp.next
        temp.next = new_node

    def deleteAtIndex(self,index):
        if index < 0 or index >= self.size:
            return

        self.size -= 1

        temp = self.head

        for _ in range(index):
            temp = temp.next

        temp.next = temp.next.next

    def get(self,index) -> int:
        if index < 0 or index >= self.size:
            return -1

        temp = self.head

        for _ in range(index + 1):
            temp = temp.next

        return temp.val
