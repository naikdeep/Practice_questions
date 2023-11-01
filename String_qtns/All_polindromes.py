def all_polindromes(str_arr):
    def check_polindrome(s):
        
        flag=False
        r_s=""
        for i in reversed(range(len(s))):
            r_s+=s[i]
        if s==r_s:
            flag=True
        return flag
    
    list_strs=[]
    for i in str_arr:
        flag = check_polindrome(i)  
        if flag == True:
            list_strs.append(i)
    print(list_strs)

    return list_strs

arr=["naik","ini",'inni','eke']
all_polindromes(arr)






