class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,head,tail,size):
        self.head = head
        self.tail = tail
        self.size = size

    def insertAtEnd(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def search(self,data):
        temp = self.head

        while(temp):
            if temp.data == data:
                return True
            temp = temp.next

    def length(self):
        temp = self.head
        len = 0

        while(temp):
            len += 1
        return len