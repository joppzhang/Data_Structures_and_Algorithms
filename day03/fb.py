# *_*coding:utf-8*_*
#求解 k 阶斐波那契数列第 m 项的值
#前k-1项为0
#第k项为1
#往后每一项为前k项的和

'''
#定义的递归方法重复的太多，耗时巨大
def fb(k,m):
	if m<k :
		return 0
	elif m==k :
		return 1
	else:
		sum=0
		for i in range(m-k,m):
			sum += fb(k,i)
		return sum
'''

'''
#k=2时候,我们可以这样改进
def fb(m):
	f=0
	g=1
	while m>0 :
		g = g+f
		f = g-f
		m = m-1
	return g
'''
#同理k阶
#fib(m)=fib(m-1)+fib(m-2)+fib(m-3)+...+fib(m-k)
#fib(m-1)   =    fib(m-2)+fib(m-3)+...+fib(m-k)+fib(m-k-1)
#fib(m)-fib(m-1) = -fib(m-k-1)+fib(m-1)
#fib(m) = 2*fib(m-1)-fib(m-k-1)
#
#
def fb(k,m):
	#假设输入合理，不合理情况可以自己加if判断
	a=list(range(0,m))
	if m<k :
		f=0
	elif m==k :
		f=1
	else:
		for i in range(0,k-1):
			a[i] = 0
		a[k-1]=1
		for j in range(k,m):
			sum=0
			for x in range(j-k,j):
				sum = sum +a[x]
			a[j]=sum
		f=a[m-1]
	return f

#Test
print(fb(3,100))


