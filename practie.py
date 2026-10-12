


class Node:
    def __init__(self, val):  # creating a node
        self.data = val
        self.next = None

class LinkedList:         # creating a link between the nodes
    def __init__(self):     
        self.head = None
        
        
    def append(self, new_node):   # append is used to add elemnt at last
        if(self.head == None):
            self.head=new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node   #appending new node

    def display(self):
        temp = self.head
        while temp:                 # display the list
            print(temp.data)
            temp = temp.next

    def insertAtPos(self, new_node, pos):
            if pos == 1:
                new_node.next = self.head               # used to insert elemet at desired position
                self.head = new_node
            else:
                temp = self.head
                p = 1
                while p < pos - 1 and temp is not None:
                    temp = temp.next
                    p += 1
                
                if temp is not None:
                    new_node.next = temp.next
                    temp.next = new_node

    def mid_node(self):
        temp = self.head            # we use the logic of first assign temp to the head and the count the nodes
                                        # and the divide the count by 2 
        count = 0
        while temp:
            count += 1
            temp = temp.next
        mid = count//2
        temp = self.head
        n=0
        while temp and n < mid:
            temp = temp.next
            n += 1
        print(temp.data)

    def del_node(self, value):
        temp = self.head
        prev = None                             # we assign temp to head check if the value passed is equal to the nodes value
                                                # if same then we delete it
        if(temp.data == value):
            self.head = self.head.next
            return
        while(temp):
            if(temp.data == value):
                break
            else:
                prev = temp
                temp =temp.next
        if temp == None:
            print("Value is not there in the list")
            return 
        prev.next = temp.next

    def reverse(self):
        curr =self.head                     # for reverse function we use the curr varialbe  to traverse
        prev = None
        while curr:
            nextnode = curr.next 
            curr.next = prev
            prev = curr 
            curr = nextnode
        self.head = prev  

    def sum_(self):
        temp = self.head
        sum=0
        while (temp and temp.next): 
            sum = temp.data + temp.next.data
            temp = temp.next
            print(sum)

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
print("Created linked list")
list.display()
print("Traverse the list using display function")
list.display()

list.insertAtPos(Node(100), 1)
print("list after insert ")
list.display()

print("Display mid node")
list.mid_node()
print("list before deletion")
list.display()
list.del_node(40)
print(" list after deletion")
list.display()
list.reverse()
print("Display reverse list")
list.display()
print("Sum of two consecutive nodes")
list.sum_()
