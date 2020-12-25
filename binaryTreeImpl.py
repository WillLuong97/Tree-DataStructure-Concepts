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


#Function to check if the tree is bst or not
def validateBST(root):
  return checkBST(root, None, None)

def checkBST(node, minValue, maxValue):
  #base case: 
  if not node:
    return True
  # Test if we're allowed to go left or right based on condition that 
  # left <= current < right
  # 2 conditions where the BST is invalid.
  # minValue == null, minValue != null, [neg infinity, 20]
  if minValue and minValue > node.data:
    return False 

  if maxValue and maxValue <= node.data: 
    return False
  
  #tree traversal: 
  #go left: 
  # recursive call to go left (and right)
  isLeftValid = checkBST(node.left, minValue, node.data)
  
  isRightValid = checkBST(node.right, node.data, maxValue)

  if not isLeftValid or not isRightValid:
    return False

  return True  



#Leetcode 617. Merge Two Binary Trees

'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.
'''
#Traverse the two tree and update a result tree with the conditions below: 
# if t1.currentNode != NULL and t2.currentNode != NUll: t1 = t1 + t2
# if t1.currentNode == NULL and t2.currentNode != NULL:  t1 = t2
# it both NULL: return NULL 
def mergeTrees(t1, t2):

    #Base case: 
    #check if the tree node are null or not
    if not t1 and  not t2: 
        return 

    if not t1: 
        return t2
    if not t2: 
        return t1

    t1.val += t2.val
    #recursion: 
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)

    return t1

#Leetcode 897. Increasing Order Search Tree

'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
 

Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
'''
def increasingBST(root):
    #helper method to traverse the tree with inorder
    def inorder(node):
        #we use yield, instead of return because the function needs to keep going.
        if node: 
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

    #dummy node
    answer = current = Node(None)

    #loop through the inorder traversal list
    for node in inorder(root):
        current.right = Node(node)
        current = current.right

    return answer.right
#Time complexity: O(N) traverse through the tree with inorder fashion, so this would cost O(n) since we must go through each time. 
#Space complexity: O(1) we need to store each node only one time
#main function to run the program
def main():
    print("Welcome to the Tree implementation structure program")
    print("")
    print("     First! We will make a tree ")
    # print(createATree())

    #Level order traversal test and driver code
    print("TESTING LEVEL ORDER TRAVERSAL...")
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(2)
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
    
    print("Checking if a tree if bst or not...")
    print(validateBST(root))
    #First tree
    t1 = Node(1)
    t1.left = Node(3)
    t1.right = Node(2)
    t1.left.left = Node(5)
    
    #Second tree: 
    t2 = Node(2)
    t2.left = Node(1)
    t2.right = Node(3)
    t2.left.right = Node(4)
    t2.right.right = Node(7)

    print("TESTING Merge Two Binary Trees...")
    
    print(mergeTrees(t1, t2))

    print("TESTING 897. Increasing Order Search Tree...")
    r = Node(5)
    r.left = Node(3)
    r.left.left = Node(2)
    r.left.left.left = Node(1)
    r.left.right = Node(4)
    r.right = Node(6)
    r.right.right = Node(8)
    r.right.right.left = Node(7)
    r.right.right.right = Node(9)
    print(increasingBST(r))
    

main()