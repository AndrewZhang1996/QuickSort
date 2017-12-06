from QuickSort import quickSort
import numpy as np

size = raw_input("Input random array size: ")
boundary = raw_input("Input upper boundary of the number in random array: ")

list_1=np.random.randint(int(boundary),size=int(size)).tolist()
list_2=np.random.randint(int(boundary),size=int(size)).tolist()
 
print("initial array:\n"+str(list_1))
quickSort(list_1,0,len(list_1)-1,'first')
print("result array:\n"+str(list_1))
print("initial array:\n"+str(list_2))
quickSort(list_2,0,len(list_2)-1,'last')
print("result array:\n"+str(list_2))