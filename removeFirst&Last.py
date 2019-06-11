list1 = [11, 5, 17, 18, 23, 50]  
unwanted_num = {11, 50}   
list1 = [ele for ele in list1 if ele not in unwanted_num] 
print("New list after removing unwanted numbers: ", list1)