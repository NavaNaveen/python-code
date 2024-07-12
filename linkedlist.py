class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode
    def prepend(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def sort(self,data):
        newnode=Node(data)
        if self.head is None or data<self.head.data:
            newnode.next=self.head
            self.head=newnode
            return
        current=self.head
        while current.next and current.next.data < data:
            current = current.next
        newnode.next = current.next
        current.next = newnode


    def delete(self,key):
        temp=self.head
        if temp is not None and temp.data==key:
            self.head=temp.next
            temp=None
            return
        prev=None
        if temp is not None and temp.data!=key:
            prev=temp
            temp=temp.next
        if temp is None:
            return
        prev.next=temp.next
        temp=None
    def dis(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    print()
if __name__=="__main__":
    linkedlist=linkedlist()
    linkedlist.sort(1)
    linkedlist.sort(5)
    linkedlist.sort(4)
    linkedlist.prepend(0)
    linkedlist.delete(1)
    linkedlist.dis()
    
       


        

