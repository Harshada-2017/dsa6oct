class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    

    def isempty(self):
        return  self.top is None
        
    def push(self,newnode):
        newnode.next=self.top
        self.top=newnode
        
    def pop(self):
        if self.isempty():
            print("Stack is empty....")
        else:
            temp=self.top
            print("Poped Element ",temp.data)
            self.top=self.top.next 
            temp=None
    def print(self):
            if self.isempty():
                print("Stack is empty...")
            else:
                print("Stack contains...")
                temp=self.top
                while temp:
                    print(temp.data)
                    temp=temp.next
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
    
    def rev_stack(s1):
        q1=lqueue()
        while not s1.isempty():
            q1.enqueue(Node(s1.pop()))
        q1.print()
            
que=lqueue()
que.enqueue(Node(12))
que.enqueue(Node(72))
que.enqueue(Node(56))
que.enqueue(Node(20))
que.enqueue(Node(17))
que.print()
que.dequeue()
que.dequeue()
                    
st=stack()
st.push(Node(10))
st.push(Node(50))
st.push(Node(70))
st.push(Node(30))
st.push(Node(40))
st.print()