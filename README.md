# Tree

## Definition:

- In computer science, a Tree is a data structure with a root value and subtree of children and parent node, represent as a set of linked nodes
- Tree is a recursive data structure.

## Structure: 
- (N) nodes will have (N-1) edges (edge are links between Node)

- Depth and height: 
    + Depth of (xth) node is the length of path from root to (xth) node or the number of edges in the path from root to X
    + Depth of root = 0

    + Height of X: is the number of edges in the longest path from x to a leaf
    + Height of a tree: is the height of a root node or the number of edges in the longest path from the root node to a leaf


## Binary Tree: 

### Definition: 
- Binary tree is a tree, in which each node can have at most 2 children

### Types of Binary Tree:
- Strict Binary Tree: each node can have only either 2 or 0 children 

```
    A               OR          A           
  B   C   
```

- Complete Binary Tree: all levels except possibly the last are completely filled with Nodes and all Nodes are as left as possible. Max number of nodes at level i = 2^i. 

Example: L - 0 = #node = 2^0 = 1
         L - 1 = #node = 2^1 = 2
         L - 2 = #node = 2^2 = 4

```
      A

   B     C

 C   D  E   F

G  H R
```

- Perfrect Binary Tree: all levels are filled with Node. Maximum number of nodes in a tree with height h = 2^ (n + 1) - 1 or 2^(number of levels) - 1

```
            A
        
        B      C
    
    D     E   F     G 
```

Find the height of a perfect binary tree: 

n = log2(n+1) - 1


### Complexity of Tree Operation:
- Minimum height = |log2(n)| where n is the number of node
- Maximum height= n - 1
- Complete/perfect tree: O(log2(n)) best case and O(n) worst case



### Balanced Binary Tree:

## Definition: 

- A balanced binary tree, also referred to as a height-balanced binary tree, is defined as a binary tree in which the height of the left and right subtree of any nodes differ by not more than 1


Example: 

![Balanced Tree](/balanced_tree.png)

+ Balanced Tree

![Not Balanced Tree](/unbalanced-binary-tree.png)





+ Unbalanced Tree






- Conditions of a balanced binary tree: 

1. The difference between the left and right subtree for any nodes is not more than 1
2. The left subtree is balanced
3. The right subtree is balanced 



### Binary Search Tree: 

## Definition: 
-   Binary tree in which for each node, the value of all the nodes in the left subtree are lesser than or equal to the root node, while all the node in the right subtree are greater than the root node. 

-   The main time complexity to work on a binary search tree is O(logn)

![Binary Search Tree](/Binary_Search_Tree.png)



## Tree traversal: 

### Breadth first search: 

- The search involves searching through a tree one level at a time. We traverse through one entire level of children nodes first, before moving onto traversing through the grandchildren nodes.

- Algorithm: there are basically two function in this method, one is to print all nodes at a given level, and one is to print the level order traversal of the tree. 

```
/*Function to print level order traversal of tree*/
printLevelorder(tree)
for d = 1 to height(tree)
   printGivenLevel(tree, d);

/*Function to print all nodes at a given level*/
printGivenLevel(tree, level)
if tree is NULL then return;
if level is 1, then
    print(tree->data);
else if level greater than 1, then
    printGivenLevel(tree->left, level-1);
    printGivenLevel(tree->right, level-1);


```

### Depth first search: 

+ Inorder traversal (Left-Root-Right):

+ Preorder traversal (Root - Left - Right):

+ Postorder traversal (Left - Right - Root):



### Time Complexity: 

- All four tree traversal algorithm requires O(n) time as they vist every node exactly onces. 


### Space Complexity: 

1.  Extra space required for the Level Order traversal is O(w), where W is the maximum width of the Binary Tree. In level order traversal, queue one by one ndoes of different level.

2.  Extra space required for Depth First Search is O(h) where h is the maximum height of the Binary Tree. In Depth First Search, stack (or function call stacks) stores ancestors of a node.  


### How to pick one? 

1. Extra space can be one factors

2. Depth first search often requires recursive function call and recursive code requires function call to overheads

3. Overall, BFS starts visiting nodes from root while DFS starts visiting nodes from leaves. So if our problem is to search through something that is more likely closer to the root, we would prefer BFS.
And if the target node is closer to the leaf, we would use DFS
