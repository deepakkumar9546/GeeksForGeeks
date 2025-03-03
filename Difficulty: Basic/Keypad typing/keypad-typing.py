#User function Template for python3


#Function to find matching decimal representation of a string as on the keypad.
def printNumber(s,n):
        ans=''
        for i in range(n):
            if s[i]=='a' or s[i] =='b' or s[i] == 'c':
                ans+='2'
            elif s[i]=='d' or s[i] =='e' or s[i] == 'f':
                ans+='3'
            elif s[i]=='g' or s[i] =='h' or s[i] == 'i':
                ans+='4'
            elif s[i]=='j' or s[i] =='k' or s[i] == 'l':
                ans+='5'
            elif s[i]=='m' or s[i] =='n' or s[i] == 'o':
                ans+='6'
            elif s[i]=='p' or s[i] =='q' or s[i] == 'r' or s[i] == 's':
                ans+='7'
            elif s[i]=='t' or s[i] =='u' or s[i] == 'v':
                ans+='8' 
            else:
                ans+='9'
        return ans
   
    #CODE HERE
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        
        s=input()
        n=len(s)
        print(printNumber(s,n))
        print("~")
# } Driver Code Ends