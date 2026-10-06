#singly linear linked list
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
            while(temp.next):
                temp=temp.next
            temp.next=new_node  #appending new node
            
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
    def sum(self):
        total=0
        temp=self.head
        
        while temp:
            total=total+temp.data
            temp=temp=temp.next
    
        return total
    
            
list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(80)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(50))
list.print()
print(list.sum())