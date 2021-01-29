#Problem 1130. Minimum Cost Tree From Leaf Values

'''
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

 

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).

'''
#Approach: we will loop through the array and multiply two pairs of number together, arr[i] and arr[i+1] and arr[i+2] arr[i], 
#then we add the product into the sum and keep repeating the process.  
def mctFromLeafValues(arr):
	#base case: 
	if not arr: 
		return 0
	
	total_sum = 0
	while len(arr) > 1:
		minIndex = 1 
		local_prod = arr[0] * arr[1]
		for i in range(2, len(arr)):
			curr_prod = arr[i-1] * arr[i]
			#keeping the smalllest product as the local product
			if curr_prod < local_prod:
				local_prod = curr_prod 
				minIndex = i
		#swap the smaller leaf node out and keep the larger leaf node in the array
		#updating the smaller value with the larger value in the array
		if arr[minIndex-1] > arr[minIndex]:
			arr[minIndex] = arr[minIndex-1]
		
		#parse the array so that it can get rid of the 
		#smaller leaf node
		arr[minIndex-1:] = arr[minIndex:]
		print(arr)
		total_sum += local_prod

	return total_sum


	
#Main function to run the program: 
def main():
	print("TESTING MINIMUM COST TREE FROM LEAF VALUES...")
	
	arr_1 = [6,2,4]
	print(mctFromLeafValues(arr_1))	
	print("END OF TESTING...")
main()
