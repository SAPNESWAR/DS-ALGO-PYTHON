def merge_list(list1,list2):
    merged_data=""
    list2.reverse()
    for i in range(len(list1)):
        if(list1[i] is None):
            list1[i]=""
        if(list2[i] is None):
            list2[i]=""
        merged_data+=str(list1[i])+str(list2[i])+" "
    return merged_data[:-1]
list1=['T','sk',None,'bl']
list2=['ue','is','y','he']
merged_data=merge_list(list1,list2)
print(merged_data)
