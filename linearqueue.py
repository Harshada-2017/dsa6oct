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
            
    def print(self):
        temp=self.front
        while temp:
            print(temp.data, end="->")
            temp=temp.next
            
que=lqueue()
que.enqueue(Node(12))
que.enqueue(Node(72))
que.enqueue(Node(56))
que.enqueue(Node(20))
que.enqueue(Node(17))
que.print()