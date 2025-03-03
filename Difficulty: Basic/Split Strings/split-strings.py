#User function Template for python3

class Solution:
    def splitString(ob, S):
        S1=""
        S2=""
        S3=""
        for i in range(len(S)):
            if(S[i].isalpha()):
                S1+=S[i]
            elif (S[i].isdigit()):
                S2+=S[i]
            else:
                S3+=S[i]
                
        return [S1,S2,S3]
        # code here 
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        ans = ob.splitString(S)
        for i in ans:
            if(i==""):
                print(-1)
            else:
                print(i)


        print("~")
# } Driver Code Ends