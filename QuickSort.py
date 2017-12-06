import threading
import time

class quickSort():

	def __init__(self, raw_list, first, last, pivot):
		self.count_last = 0
		self.count_first = 0
		if pivot == 'first':
			self.QuickSort_first_pivot(raw_list, first, last) # space complexity: n + 5 time complexity: n^2/2+7n/2+3
			print("Comparisions (first as pivot): " + str(self.count_first))
		if pivot == 'last':
			self.QuickSort_last_pivot(raw_list, first, last) # space complexity: n + 5 time complexity: n^2/2+7n/2+1
			print("Comparisions (last as pivot): " + str(self.count_last))

	def QuickSort_first_pivot(self, list, first, last):
		if first<last: # check whether the first index is smaller than last index
			divIndex=self.Partition_first_pivot(list,first,last) # 4n + 1 ## divide the list into two lists by the splitpoint
			#print(list)
			#print(divIndex)
			#both of two are ((n^2-n)/2)
			self.QuickSort_first_pivot(list,first,divIndex-1) # do recursion on the front part
			self.QuickSort_first_pivot(list,divIndex+1,last) # do recursion on the back part
		else:
			return # 1

	def Partition_first_pivot(self, list, first, last):
	    i=first # 1 # make the i equals to first index
	    mutex = threading.Lock() # create a mutex
	    for j in range(first+1,last+1): # n-1 # for all element after the first element in the list
	    	mutex.acquire() # lock
	    	self.count_first += 1 # count comparision step
	    	mutex.release() # unlock
	    	
	    	#print(list[j])
	        if list[j]<=list[first]: # n-1 # if the element is smaller than the first (pivot)
	            i=i+1 # n-1 # move the i to the right for one
	            list[i],list[j]=list[j],list[i] # n-1 # exchange the i element and the j element for make the element which is smaller than pivot move to the front of the splitpoint
	    list.insert(i+1, list[first]) # 1 # move the pivot to the splitpoint
	    del list[first] # 1 delete the first element
	    return i # 1

	def QuickSort_last_pivot(self, list, first, last):
	    if first<last: # 1
	        divIndex=self.Partition_last_pivot(list,first,last) # 4n-1
	 
	 		#sum of two are ((n^2-n)/2)
	        self.QuickSort_last_pivot(list,first,divIndex)       
	        self.QuickSort_last_pivot(list,divIndex+1,last) 
	    else:
	        return # 1
 

	def Partition_last_pivot(self, list, first, last):
	    i=first-1 # 1
	    mutex = threading.Lock()
	    for j in range(first,last): # n-1
	    	mutex.acquire()
	    	self.count_last += 1
	    	mutex.release()
	        if list[j]<=list[last]: # n-1
	            i=i+1 # n-1
	            list[i],list[j]=list[j],list[i] # n-1
	    list[i+1],list[last]=list[last],list[i+1] # 1
	    return i # 1











