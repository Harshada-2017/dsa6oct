class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def append(self,newnode):
        if(self.head==None):
            self.head=newnode
        else:
            temp=self.head
            while(temp.next):# karan temp.next null jo paryant hott ani
                temp=temp.next # to paryant temp is temp.next
            temp.next=newnode# jevha none hoil tevha temp.next=newnode
            
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
        
    def sum(self):
            total=0
            temp=self.head
            
            while temp:
                total=total+temp.data
                temp=temp.next
        
            return total
            
            
list=Linkedlist()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.print()
print(list.sum())