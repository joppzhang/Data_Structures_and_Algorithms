#*_*coding:utf-8*_*
#快速排序的原始递归版
def swap(a,b):
	a=a^b
	b=a^b
	a=a^b
	return a,b

def quick_sort(a):
	if len(a) ==1 :
		return a
	else:
		i=0
		key = a[0]
		for j in range(1,len(a)):
			if a[j] <= key :
				a[j],a[i+1] = swap(a[j],a[i+1])
				i=i+1
		a[0],a[i] = swap(a[0],a[i])
		if i==0 :
			return [a[0]]+quick_sort(a[1:])
		elif i==len(a)-1:
			return quick_sort(a[:len(a)-1])+[a[len(a)-1]]
		else:	
			b=a[0:i]
			c=a[i+1:]
			return quick_sort(b)+[a[i]]+quick_sort(c)

#Test
a=[6,5,34,3,1,12,23,11,4,23,65,23,87,34,453,23,9,123,34,34,21,3,3,765,32,3,654,2,3,23,4,65,27,90]
print(quick_sort(a))

