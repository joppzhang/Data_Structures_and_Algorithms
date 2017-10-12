# *_*coding:utf-8*_*
#求解ai*x^i (i=0,1,2……)的和
def sum_pow(a,x,n):
	#原始版
	'''
	sum=0
	for i in range(0,n):
		sum += a[i]*pow(x,i)
	return sum
	'''
	#改进版
	sum = 0
	for i in range(n,0,-1):
		sum  = sum * x + a[i-1]
		i=i-1
	return sum
#Test
print(sum_pow([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],4,5))