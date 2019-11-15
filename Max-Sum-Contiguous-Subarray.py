class Solution:
    # @param A : tuple of integers
    # @return an integer
	# this is solved using kadane's algorithm
    def maxSubArray(self, A):
       maxSum = A[0]
       sumSoFar = 0

       for i in A:
           if ((sumSoFar < 0 )  and ( sumSoFar < i)):
               sumSoFar = 0

           sumSoFar += i

           if (sumSoFar > maxSum):
               maxSum = sumSoFar

       return maxSum
