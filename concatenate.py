class Node:
    def __init__(self,val): #constructor
        self.data=val #nodes data is equal to 10 (suppose to take value 10)
        self.next=None # next will be null because i don't know if there is next  node or i will create next node

class LinkedList:
    def __init__(self):
        self.head=None # head is none
        
    def append(self,new_node):
        if(self.head==None):
            self.head=new_node
           
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node  #appending new node
            
    def concatenate(self,list2):
        if self.head==None:
            self.head=list2.head
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=list2.head
        
            
    def print(self):
                        temp=self.head
                        while temp:
                            print(temp.data)
                            temp=temp.next
                            
list=LinkedList()
list2=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(80)
n4=Node(100)
n5=Node(17)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(n5)
list2.append(n1)
list2.append(n2)
list2.append(n3)
list2.append(n4)
list2.append(n5)

list.print()
list.concatenate(list2)
list.print()