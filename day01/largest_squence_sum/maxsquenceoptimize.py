# *_*coding:utf-8*_*
#优化寻找最大值的算法，时间复杂度O(n)
def max_squence_optimize(arr):
	maxSum = 0;   
	thisSum = 0;   
	for j in range(0,len(arr)):  
		thisSum = thisSum + arr[j]; 
		#print ('thissum:',thisSum)  #输出过程中的值有助于理解代码执行过程
		if thisSum>maxSum:   
			maxSum = thisSum 
			#print('maxSum:',maxSum)  #输出过程中的值有助于理解代码执行过程
		elif thisSum < 0:
			thisSum = 0 
	return maxSum;

print (max_squence_optimize([0, -3, 6, 8, -20, 21, 8, -9, 10, -1, 3, 6, 5]))