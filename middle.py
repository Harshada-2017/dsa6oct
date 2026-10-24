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
            
    def findmid_del(self):
        temp=temp1=self.head
        prev=None                       # find the middle node and del the middle node
        while temp1 and temp1.next:
            prev=temp
            temp1=temp1.next.next
        print("Middle Node: ",temp.data)
        prev.next=temp.next
        temp=None
        
    def firstandlast(self):
        temp1=self.head
        temp1=None
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        temp=None
            
            
    def del_node(self,value):
            temp=self.head
            if temp.data==value:
                self.head=self.head.next
                return
            while(temp):
                if temp.data==value:
                    break
                else:
                    prev=temp
                    temp=temp.next
            if temp==None:
                print("Value is not present in the list")
                return
            prev.next=temp.next
            temp=None
                
    def print(self):
                temp=self.head
                while temp:
                    print(temp.data)
                    temp=temp.next
          
                
list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(80)
list.append(n1)
list.append(n2)
list.append(n3)
list.print()
list.firstandlast()
list.print()
list.firstandlast
list.print()
list.del_node(20)
list.print()
    #list.insert(Node(100),1)
    #list.print()   