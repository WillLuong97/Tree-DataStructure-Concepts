#This is a Python implementation of how to set up a Binary tree and detemine if a tree is what kind of tree

COUNT = [10]

#A python class that represents an individual node:
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


#function to print a tree to the console
def print2D(root):
    print2DUtil(root, 0)

#Helper method to print the tree out
def print2DUtil(root, space):
    #Base case: if the tree is empty the there are nothing to print out
    if (root == None):
        return

    #increase the space between levels:
    space += COUNT[0]

    #Process the right child first
    print2DUtil(root.right, space)
    #print the current node after space
    #count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    #process the left child
    print2DUtil(root.left, space)    



#basic function to create a tree
def createATree():
    #create a root: 
    root = Node(1)
    ''' following is the tree after above statement 
              1 
            /   \ 
            None  None'''  
    root.left = Node(2)
    root.right = Node(3)
    ''' 2 and 3 become left and right children of 1 
            1 
            /   \ 
            2      3 
        /    \    /  \ 
    None None None None'''

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print2D(root)

#main function to run the program
def main():
    print("Welcome to the Tree implementation structure program")
    print("")
    print("     First! We will make a tree ")
    print(createATree())
    
main()