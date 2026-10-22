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
        
    def print(self):
        if self.isempty():
            print("Stack is empty...")
        else:
            print("Stack contains...")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
                
    def rev(self):
        temp=self.top
        while temp:
            st1.push((Node(temp.data)))
            prev=temp
            temp=temp.next
        
st=stack()
st1=stack()
st.push(Node(10))
st.push(Node(50))
st.push(Node(70))
st.push(Node(30))
st.push(Node(40))
st.print()
st.rev()
st1.print()