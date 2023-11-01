def allAnagrams(arr):
    def frequencyGen(str1):
        fre_dict={}
        for i in str1:
            if i in fre_dict:
                fre_dict[i]+1
            else:
                fre_dict[i]=1
        return fre_dict
    fre_list=[]
    for str2 in arr:
        
        freq_dict=frequencyGen(str2)
        fre_list.append(freq_dict)
    #print(fre_list)

    dict_grouped=[]
    ct=0
    trues=1
    while (ct<len(fre_list)):
       temp_arr=[]
       temp_arr.append(fre_list[ct])
       in_ct=ct+1
       while(in_ct<len(fre_list)):
           if fre_list[ct]==fre_list[in_ct]:
               #print(in_ct)
               #print(fre_list)
               temp_arr.append(fre_list[in_ct])
               #if not (len(fre_list)-2)==in_ct:
               fre_list.remove(fre_list[in_ct])
               #print(in_ct)
           in_ct+=1
       print(fre_list)

       dict_grouped.append(temp_arr)
       ct+=1
       #dict_grouped.remove(dict_grouped[-1])
    return dict_grouped

        



               

      

arr=["gaot","goat","not","ton","gem","care","acre","reca"]
print(allAnagrams(arr))
        
                

