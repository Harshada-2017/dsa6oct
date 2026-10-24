# linear queue using linked ist

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
class lqueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
            
    def dequeue(self):
        temp=self.front
        print("deleted node",temp.data)
        self.front=self.front.next 
        if self.front==None:  #m if ther is only one node that we are deleting
            print("Queue is empty")
            self.rear=None
        temp=None 
            
    def print(self):
        temp=self.front
        while temp:
            print(temp.data, end="->")
            temp=temp.next 
        print()
            
que=lqueue()
que.enqueue(Node(12))
que.enqueue(Node(72))
que.enqueue(Node(56))
que.enqueue(Node(20))
que.enqueue(Node(17))
que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()