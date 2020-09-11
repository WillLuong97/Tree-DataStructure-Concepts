#This python3 program will create and determine if a tree is height balanced or not
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class calculateHeight():
    def __init__(self):  
        self.calculateHeight = 0


def isHeightBalancedTree(root, height):
    #base case: the height only has 1 root: 
    if not root: 
        return True

    #checking the height of both the left and right subtree
    left_height = calculateHeight()
    right_height = calculateHeight()
    #recursively check for height balanced tree condition across the element
    l = isHeightBalancedTree(root.left, left_height)
    r = isHeightBalancedTree(root.right, right_height)
    #check if the height of the left and the right subtree would be equal to lesser than 1
    calculateHeight.calculateHeight = max(left_height.calculateHeight, right_height.calculateHeight) + 1

    if abs(left_height.calculateHeight - right_height.calculateHeight) <= 1:
        return l and r


    return False



#driver code to create and test if a tree is height balanced: 
def main():
    print('TESTING HEIGHT BALANCED TREE...')
    print("TREE 1 INSERTED")
    #inserting a tree:
    CalculateHeight = calculateHeight()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    if isHeightBalancedTree(root, calculateHeight):
        print("Tree1 is a height balaned tree!")

    else:
        print("Tree1 is not height balanced")
    print("END OF TESTING...")
main()