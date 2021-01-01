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

```
1. Traverse the left subtree, i.e. call Inorder(left-subtree)
2. Visit the root 
3. Traverse the right subtree, i.e. call Inorder(right-subtree)
```

- Uses of Inorder: In case of binary search tree (BST), Inorder traversal gives nodes in non-decreasing order. To get nodes of BST in a non-decreasing matter, a variation of inorder traversal where inorder traversal is reversed can be used. 

+ Preorder traversal (Root - Left - Right):

```
Algorithm Preorder(tree)
1. Visit the root.
2. Traverse the left subtree, i.e., call Preorder(left-subtree)
3. Traverse the right subtree, i.e., call Preorder(right-subtree) 
```
- Uses of Preorder: Preorder traversal is used to create a COPY of a tree. Preoder traversal is also used to get PREFIX expression on of an expression tree. 


+ Postorder traversal (Left - Right - Root):

```
Algorithm Postorder(tree)
1. Traverse the left subtree, i.e., call Postorder(left-subtree)
2. Traverse the right subtree, i.e., call Postorder(right-subtree)
3. Visit the root.

```

- Uses of Postorders: 
- Is used to DELETE a tree. It is also useful to get the POSTFIX expression of an expression tree.  


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


## N-ary Tree

### Definition

- A binary tree is an N-ary tree if a tree is a rooted tree and each node has no more than N children. 


![N-ary tree example](/nary_tree_example.png)


- Trie is one of the most frequently used N-ary tree 
- A binary tree is a form of an N-ary tree. 


### Tree Traversal
- A binary tree can be traversed in preorder, inorder, postorder or level-order. Among these traversal algorithm, preorder, postorder, and level-order traversal are more suitable to be extended to a N-ary tree. 


### Classical Recursion Solution

1. "Top-down" Solution

```
"Top-down" means that in each recursion level, we will visit the node first to come up with some values, and parse these values to its children when calling the function recursively.

```

Algorithm

```
1. return specific value for null node
2. update the answer if needed                // answer <-- params
3. for each child node root.children[k]:
4.    ans[k] = top_down(root.children[k], new_params[k])  // new_params <-- root.val, params
5. return the answer if needed                // answer <-- all ans[k]
```


2. "Bottom-up" solution

```
"Bottom-up" means that in each recursion level, we will firstly call the functions recursively for all the children nodes and then come up with the answer according to the return values and the value of the root node itself.
```

A typical "bottom-up" recursion function ```bottom_up(root)``` work like this: 

```
1. return specific value for null node
2. for each child node root.children[k]:
3.    ans[k] = bottom_up(root.children[k])  // call function recursively for all children
4. return answer                // answer <- root.val, all ans[k]
```











