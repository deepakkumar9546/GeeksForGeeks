#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        red=0
        green=0
        
        for i in S:
            if(i=='R'):
                red+=1
            else:
                green+=1
            
        if(red>green):
            return green
        else:
            return red
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()
        
        ob=Solution()
        print(ob.RedOrGreen(N,S))
        print("~")
# } Driver Code Ends