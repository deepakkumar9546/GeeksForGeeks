#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, x):
        i, j = 0, len(arr2) - 1  # Two pointers: left for arr1, right for arr2
        cnt = 0

        while i < len(arr1) and j >= 0:
            pair_sum = arr1[i] + arr2[j]
            
            if pair_sum == x:
                cnt += 1
                i += 1  # Move left pointer forward
                j -= 1  # Move right pointer backward
            elif pair_sum < x:
                i += 1  # Increase sum by moving left pointer
            else:
                j -= 1  # Decrease sum by moving right pointer
        
        return cnt
                    
        #code here.



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x = int(input())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        l = ob.countPairs(arr1, arr2, x)
        print(l)
        print("~")

# } Driver Code Ends