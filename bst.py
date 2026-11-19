# Binary search tree
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None: # creating the root node
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left #it will go to next level
                else:
                    if  temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right #it will go to next level
    
def inorder(temp): #recursive
    if temp is None:
        return
    else:
        inorder (temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)
btree=BST()
btree.insert(Node(10))
btree.insert(Node(50))
btree.insert(Node(5))
btree.insert(Node(17))
btree.insert(Node(20))
btree.insert(Node(3))
inorder(btree.root)
