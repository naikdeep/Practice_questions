class AlphaNumers():
    def __init__(a,s):
        a.s=s
    def sumOfNumersInStr(a):
        i=0
        n=len(a.s)-1
        sum=0
        while(i<n-1):
            j=i+1
            if (ord(a.s[i])>=48 and ord(a.s[i])<=57):
                
                num=ord(a.s[i])-48
                
                while(ord(a.s[j])>=48 and ord(a.s[j])<=57 and j<n-1):
                    num=num*10
                    num=num+(ord(a.s[j])-48)
                    j+=1

                if ((j==n-1) and ord(a.s[j])>=48 and ord(a.s[j])<=57 ):
                   print(num)
                   num=num*10
                   num=num+(ord(a.s[j])-48)
                sum+=num
            i=j
        return sum
    
    
obj1=AlphaNumers("1654asf")
print(obj1.sumOfNumersInStr())

                


