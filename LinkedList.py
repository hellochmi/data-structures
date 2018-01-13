class LinkedList(object):

    # always initialize with null values in data fields
    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def add(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size += 1

    def show(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next

    def insert(self,data):
        
    def delete(self,data):
        

    def sort(self,data):

## Set previous as None, current as head and next as the next node of current
## Iterate through the linked list until current is None (this is the loop’s exit condition)
## During each iteration, set the next node of current to previous
## Then, set previous as current, current as next and next as its next node (this is the loop’s iteration process)
## Once the current becomes None, set the head pointer to the previous node.

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = current.nxt
            current.nxt = prev 
            prev = curr
            curr = nxt

        return prev

class Node(object):

    # initialize with null values
    def __init__(self, data=None, nextnode=None):
        self.data = data
        self.next = nextnode
       


