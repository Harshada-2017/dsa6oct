class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value 
        self.next=None
        
class LinledList:
    def __init__(self):
        self.head=None
        
    def append(self,new_node):
        temp=self.head
        if temp: # temp is not none mg while loop execute honar ani asel null tar mg else block honar
            while temp.next:
                temp=temp.next 
            temp.next=new_node
            new_node.prev=temp
            
        else: #First node
            self.head=new_node
            
    def print(self):
            temp = self.head
            print("Lis elements: ")
            while temp is not None:
                print(temp.data," ")
                temp = temp.next     
                
list1=LinledList()
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(36))
list1.append(Node(85))
list1.print()