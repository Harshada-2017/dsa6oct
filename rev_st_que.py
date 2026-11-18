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
            popped_data=temp.data
            self.top=self.top.next 
            temp=None
            return popped_data
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
    def isempty(self):
            return  self.front is None
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
            
    def dequeue(self):
        temp=self.front
        print("deleted node",temp.data)
        dequed_data=temp.data
        self.front=self.front.next 
        if self.front==None:  #m if ther is only one node that we are deleting
            print("Queue is empty")
            self.rear=None
        temp=None 
        return dequed_data
    def print(self):
        temp=self.front
        while temp:
            print(temp.data, end="->")
            temp=temp.next 
        print()
    
def rev_stack(s1):
    q1=lqueue()
    while not s1.isempty(): # pop from stack and enqueue to queue
        q1.enqueue(Node(s1.pop()))
    #q1.print()
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    s1.print()    


                  
st=stack()
st.push(Node(10))
st.push(Node(50))
st.push(Node(70))
st.push(Node(30))
st.push(Node(40))
st.print()
rev_stack(st)