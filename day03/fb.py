#求解 k 阶斐波那契数列第 m 项的值
#前k-1项为0
#第k项为1
#往后每一项为前k项的和

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
print(fb(3,6))


