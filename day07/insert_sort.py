#*_*coding:utf-8*_*



def insert_sort(a):
	for i in range(1,len(a)):
		key = a[i]
		j=i-1
		while j>=0 :
			if a[j] > key:
				a[j+1] = a[j]
				a[j] = key 
			j -= 1
	return a




#Test
a=[6,3,2,67,32,1,87,342,433,24,642,654,68,6,23,435,744,2343,5]
print(insert_sort(a))
