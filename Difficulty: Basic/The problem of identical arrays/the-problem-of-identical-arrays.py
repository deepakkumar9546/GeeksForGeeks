#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
# arr1 number[] 
# arr2 number[] 
# return boolean
class Solution:
    def isIdentical(self, a, b):
        #Your code goes here.
        a.sort()
        b.sort()
        
        return a==b


#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        solution = Solution()
        if solution.isIdentical(arr1, arr2):
            print("true")
        else:
            print("false")
        print("~")

if __name__ == "__main__":
    main()
# } Driver Code Ends