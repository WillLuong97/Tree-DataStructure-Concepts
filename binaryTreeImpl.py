#This is a Python implementation of how to set up a Binary tree and detemine if a tree is what kind of tree

COUNT = [10]

# #A python class that represents an individual node:
# class Node:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.val = value


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




#Recursive function to implement level order traversal of a binary search

#A node structure: 
class Node:
    #utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

"""
Helper method to find the height of a tree--the number of nodes along
the longest path from the root node to the farthest leaf node
"""
def treeHeight(node):
    #if the tree is empty, then return 0
    if not node:
        return 0

    else:
        #base case: 
        left_height = treeHeight(node.left)
        right_height = treeHeight(node.right)

        #height of the sub tree, left and right
        if left_height > right_height:
            return left_height + 1

        else:
            return right_height + 1


#Function to print out all the level order traversal of a tree: 
def printLevelOrder(root):
    h = treeHeight(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)

#Level order traversal algorithm: 
def printGivenLevel(root, level):
    if not root: 
        return 0

    if level == 1:
        print(root.data,end=" ")

    elif level > 1: 
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)



#A function to do inorder tree traversal: 
def printInorder(root):
    #if the tree contains element in it:
    if root:

        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)


#A function to do preorder traversal: 
def printPreOrder(root):
    if root:
        print(root.data, end =" ")
        printPreOrder(root.left)
        printPreOrder(root.right)


#A function to do Postorder tree traversal: 
def printPostOrder(root):
    if root: 
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.data, end=" ")


 


#main function to run the program
def main():
    # print("Welcome to the Tree implementation structure program")
    # print("")
    # print("     First! We will make a tree ")
    # # print(createATree())

    #Level order traversal test and driver code
    print("TESTING LEVEL ORDER TRAVERSAL...")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Level order traversal of binary tree is: ")
    printLevelOrder(root)
    print()
    print("TESTING DEPTH FIRST SEARCH....")
    print("Preorder traversal of binary tree is: ")
    printPreOrder(root)
    print()

    print("Inorder traversal of a binary tree is: ")
    printInorder(root)
    print()

    print("Postorder traversal of a binary tree is: ")
    printPostOrder(root)
    
    
main()