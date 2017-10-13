# *_* coding : utf-8 *_*

#select_sort是冒泡排序的一种改进。

def swap(a,b):
	a=a^b
	b=a^b
	a=a^b
	return a,b
'''

def bubble_sort(a):
	
	for i in range(0,len(a)-1):
		for j in range(i+1,len(a)):
			if a[j]<a[i] :
				#冒泡排序这里每次一步，只能一小步一小步的移动，
				#我们把他做成一大步就是下面的选择排序
				a[i],a[j]=swap(a[i],a[j])	
	return a
'''

def select_sort(a):
	
	for i in range(0,len(a)-1):
		min = i
		for j in range(i+1,len(a)):
			if a[j]<a[min] :
				min = j
		a[i],a[min]=swap(a[i],a[min])		
	return a

#Test
a=[766,2,5,4,89,7,8,54,67,43,6,87,34,9,456,8,565,34,23,876,345,254]
print(select_sort(a))


