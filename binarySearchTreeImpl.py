#Python3 implementation of binary search tree approach: 
#Tree node implementation: 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #print the tree structure:
    #level-order (Breadth first search)
    def printTreeNode(self):
        if self.left: 
            print(self.left.printTreeNode())

        print(self.data)

        if self.right:
            print(self.right.printTreeNode())

    #tree traversal: DFS
    def printTreeNode_INORDER(self, root):
        result = []
        if root:
            result = self.printTreeNode_INORDER(root.left) 
            result.append(root.data)
            result += self.printTreeNode_INORDER(root.right)
        return result

    def printTreeNode_POSTORDER(self, root):
        result = []
        if root:
            result = self.printTreeNode_POSTORDER(root.left)
            result += self.printTreeNode_POSTORDER(root.right)
            result.append(root.data)
        return result

    def printTreeNode_PREORDER(self, root):
        result = []
        if root: 
            result.append(root.data)
            result += self.printTreeNode_PREORDER(root.left)
            result += self.printTreeNode_PREORDER(root.right)
        return result
    #function to check if a binary tree is a bst or not:
    def validateBST(self, root):
        #base case: 
        if not root: 
            return None
        auxilaryArr = self.printTreeNode_INORDER(root)
        #loop through the array and check for the conditions 
        for i in range(len(auxilaryArr) - 1):
            if auxilaryArr[i] < auxilaryArr[i-1]:
                return False

        return True

    #700. Search in a Binary Search Tree
    '''
        Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

    For example, 

    Given the tree:
        4
        / \
        2   7
        / \
        1   3

    And the value to search: 2
    You should return this subtree:

        2     
        / \   
        1   3
    In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

    Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
    '''
    def searchBST(self, root, val):
        def helper(root, val):
            #base case:
            #if the tree is empty, returns an empty string
            if not root: 
                return

            if root.val == val: 
                return root

            if val < root.val: 
                return self.searchBST(root.left, val)   

            return self.searchBST(root.right, val)
        return helper(root, val)

#time complexity: O(N)
#space comeplexity: O(n) the recursion stack is created the element is found.



#main fucntion to run the test cases: 
def main():
    print("***BINARY SEARCH TREE IMPLMENTATION***")

    root = Node(1)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(5)

    #print(root.printTreeNode())
    print("TREE TRAVERSAL USING INORDER: ")
    print(root.printTreeNode_INORDER(root))
    print("TREE TRAVERSAL USING INORDER: ")
    print(root.printTreeNode_POSTORDER(root))
    print("TREE TRAVERSAL USING INORDER: ")
    print(root.printTreeNode_PREORDER(root))
    print("Check if a tree is BST or not: ")
    print(root.validateBST(root))
    print("**END OF PROGRAM***")
main()
