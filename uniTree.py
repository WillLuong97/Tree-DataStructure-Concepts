#Problem 965. Univalued Binary Tree


'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false
 

Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].

'''
#Tree node structure: 
class Node():
        def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right


#the approach: using BFS, we would be able to keep track of all the node element and compare them with the root node, as it is the 
#value we picked to compare with
def isUnivalTree(root):
        #base case:
        if not root:
                return False
        #a queue to store each element in the tree and compare it with the 
        #anchor value
        queue = [root]
        while queue:
                for _ in range(len(queue)):
                        current_node = queue.pop(0)
                        if current_node.val != root.val:
                                return False
                        if current_node.left: queue.append(current_node.left)
                        if current_node.right: queue.append(current_node.right)

        return True


#DFS approach: root -> left-> right
#Time complexity: O(n)
#Space complexity: O(n)
def isUnivalTree(root):
        #base case: 
        if not root:
                return False
        val = []
        def dfs(root):
                if root:
                        val.append(root.val)
                        dfs(root.left)
                        dfs(root.right)

        dfs(root)
        return len(set(val)) == 1

"unTree.py" 80L, 1573C

