from functools import reduce
  
def Average(lst): 
    return reduce(lambda a, b: a + b, lst) / len(lst) 
  
 
lst = [15, 9, 55, 41, 35, 20, 62, 49] 
average = Average(lst) 

print("Average of the list =", round(average, 2)) 