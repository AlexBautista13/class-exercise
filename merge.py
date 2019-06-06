def merge(list1, list2): 
      
    merged_list = tuple(zip(list1, list2))  
    return merged_list 
      
# Driver code 
list1 = [1, 2, 3] 
list2 = ['a', 'b', 'c'] 
print(merge(list1, list2)) 