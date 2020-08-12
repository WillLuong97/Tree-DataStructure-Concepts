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
