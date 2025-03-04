#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends

#User function Template for python3
class Solution:
    def rowSum(self, mat):
        result=[]
        for row in mat:
            row_sum=0
            for num in row:
                row_sum+=num
                
            result.append(row_sum)
            
        return result
            


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        m = int(input())
        mat = [list(map(int, input().split())) for _ in range(n)]
        sln = Solution()
        ans = sln.rowSum(mat)
        print(" ".join(map(str, ans)))
        print("~")
# } Driver Code Ends