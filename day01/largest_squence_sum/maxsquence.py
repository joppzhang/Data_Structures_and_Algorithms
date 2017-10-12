# *_*coding:utf-8*_*
#最大子序列和
#最简单的一种方法就是把所有子序列和求出来，找到最大值。时间复杂度为O(n^2)
def maxsquence(arr):
	squence = []
	maxsum = 0
	for i in range(0,len(arr)):
		#如果前面是负数，就不考虑加进去了
		if arr[i]>0:
			this_sum = 0
			for j in range(i,len(arr)):
				#每次找到从i开始到最后的所有子序列的和最大值。
				this_sum = this_sum + arr[j]
				if this_sum > maxsum :
					maxsum = this_sum
	return maxsum

print (maxsquence([0, -3, 6, 8, -20, 21, 8, -9, 10, -1, 3, 6, 5]))

