# *_*coding:utf-8*_*
#冒泡排序的优化

def swap(a,b):
	a=a^b
	b=a^b
	a=a^b
	return a,b

'''
#普通版
def bubble_sort(a,lo,hi):
	flag = True
	while flag :
		flag = False
		for i in range(lo+1,hi):
			if a[i-1] > a[i]:
				a[i-1],a[i]=swap(a[i-1],a[i])
				flag = True
	return a

'''

#优化版，每次遍历后记录最后一次的交换位置，那么说明后面的数据已经排好序，从而减少排序次数
def bubble(a,lo,hi):
	last = lo
	for i in range(lo,hi-1):
		if a[i] > a[i+1] :
			last = i
			a[i],a[i+1]=swap(a[i],a[i+1])
	return last
def bubble_sort(a,lo,hi):
	while lo<hi :
		hi=bubble(a,lo,hi);
	return a


#Test
a=[1,6,3,9,4,7,0,6,3,5,2,4,5,6,7,8,9,23,35,234,1,5432,3,1231,34,2,4,64,23,345,543,245,66,234,78,653,423,4234,98]
print(a)
print(bubble_sort(a,0,len(a)))