class PolindromicSubstring():
    def LongestPolindromicSubsequnece(self,s):
        n=len(s)
        L,R=0
        for i in range(len(s)):
            l,r=i-1,i
            while(i<n):
                if (l>0 and s[l]==s[r]):
                    L,R=l,r
                    l-=1
                    r+=1
                else:
                    break
                i+=1
            if (L+R-1<l+r-1):
                L,R=l+1,r-1
                    
                
                
            


