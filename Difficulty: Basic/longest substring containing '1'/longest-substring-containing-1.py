#User function Template for python3

def maxlength(s):
    c=0
    a=0
    for i in s:
        if(i=='1'):
            c+=1
        else:
            a=max(c,a)
            c=0
        
    return max(a,c)
            
        
    
    #add code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        s=input()
        print(maxlength(s))
        print("~")
# } Driver Code Ends