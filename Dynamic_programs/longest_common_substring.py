def  longest_common_substring(s1,s2):
    n1=len(s1)
    n2=len(s2)
    if (n1==0) or  (n2==0):
        return 0
    lookMat=[[0]*(n1+1) for i in range(n2+1)]
    print(lookMat)
    longest_string=0
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            #print(i,j)
            
            """if s1[i]==s2[j] and ((i==0) or (j==0)):
                print(i,j)
                lookMat[i][j]=1
            elif s1[i]==s2[j]:"""

            if s1[i-1]==s2[j-1]:
                lookMat[j][i]=1+lookMat[j-1][i-1]
                longest_string=max(longest_string,lookMat[j][i])
                
    return longest_string

print(longest_common_substring("naik","mynameisnaik"))






