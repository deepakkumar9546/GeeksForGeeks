#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
    def findUnion(self,a, b):
        #Your code here
        union_list=set(a).union(set(b))
        
        return sorted(union_list)


#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        if(len(li)==0):
            print("[]")
            continue
        for val in li:
            print(val, end=' ')
        print()
# } Driver Code Ends