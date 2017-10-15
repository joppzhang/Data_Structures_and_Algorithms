#*_*coding : utf-8*_*

#归并算法
def merge(a,b):
	c=list(range(0,len(a)+len(b)))
	i=0
	j=0
	while i != len(a) and j != len(b) :
		if a[i]<b[j] :
			c[i+j]=a[i]
			i=i+1
		else :
			c[i+j]=b[j]
			j=j+1
	if i==len(a) :
		for x in range(j,len(b)) :
			c[len(a)+x] = b[x]
	if j==len(b) :
		for x in range(i,len(a)) :
			c[len(b)+x] = a[x]
	return c;
'''
#递归实现排序,
def merge_sort(a):
	if len(a)<=1 :
		return a
	mid = int(len(a)/2)
	left = a[:mid]
	right = a[mid:]
	left = merge_sort(left)
	right = merge_sort(right)
	return merge(left,right)
'''
#迭代实现,进行改进
def merge_sort(a):
	length = len(a)
	step = 1
	while step < length :
		hi = step << 1
		mid = step
		for i in range (0,length,hi):
			a[i:i+hi] = merge(a[i:i+mid],a[i+mid:i+hi])
		step = hi
	return a

#Test
a=[234,74,2347,54,234,987,4,3,2,9,46,45,6,435,24,853]
print(merge_sort(a))


