# *_*coding:utf-8*_*
#寻找一个数组中最小值的索引
def find_simmallest(arr):
	smallest = arr[0]
	index = 0
	for i in range(1,len(arr)):
		if arr[i]<smallest:
			smallest=arr[i]
			index=i
	return index

def sort(arr):
	newArray = []
	index=0
	for i in range(len(arr)):
		#找到最小值索引
		index = find_simmallest(arr)
		#删掉最小值并添加到新集合
		newArray.append(arr.pop(index))
	return newArray

arr = sort([1,2,5,2,7,3,0,9,56,32,76,32,87,213])
print (arr)