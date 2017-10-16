# *_*coding:utf-8*_*
# 快速排序的代码精简递归版
def quickSort(arr):
	if len(arr)<2:
		return arr
	else:
		p = arr[0]
		#将大于轴的和小于轴的数据分类成两个数组
		small = [i for i in arr[1:] if i<p ]
		large = [i for i in arr[1:] if i>=p]
	return quickSort(small) + [p] + quickSort(large)

print (quickSort([1,2,6,4,3,45,3,24,63,1,754,23,475,34,4354,5234,43,234,354,35]))