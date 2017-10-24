#*_*coding:utf-8*_*
#
#二叉树计算表达式，将中缀表达式转换成逆波兰表达式
#（只考虑+-*/和不考虑带括号的简单情况）

#定义二叉树节点
class BTNode(object):
	def __init__(self,data):
		self.data = data
		self.l = None
		self.r = None

#通过中缀表达式建立二叉树
class BuildTree(object):
	def __init__(self,l):
		self.l=l
	def build(self,l):
		if len(l)==0:
			return None
		if len(l)==1:
			return BTNode(l[0])
		posion=0
		hasplus=0
		for i in range(0,len(l)):
			if l[i]=='+' or l[i]=='-':
				hasplus=hasplus+1
				posion=i
		if hasplus==0:
			for j in range(0,len(l)):
				if l[j]=='*' or l[j]=='/':
					hasplus=hasplus+1
					posion=j		
		p=BTNode(l[posion])
		p.l=self.build(l[:posion])
		p.r=self.build(l[posion+1:])
		return p

#之前写好的栈，用来计算逆波兰表达式的值
class Stack(object) :
	def __init__(self,size):
		#类的构造函数
		self.size = size
		self.stack = []
	def __str__(self):
		#类的字符串输出方法，类似于java的.toString()方法
		return str(self.stack)
	def getSize(self) :
		#获取栈当前大小
		return len(self.stack)
	def push(self, x) :
		#入栈，栈满抛异常
		if self.isfull() :
			#return -1
			raise Exception("Stack is full")
		self.stack.append(x)
	def pop(self) :
		#出栈，栈空抛异常
		if self.isempty() :
			#return -1
			raise Exception("Stack is empty")
		topElement = self.stack[-1] 
		self.stack.remove(topElement)
		return topElement
	def isempty(self) :
		#判断栈空
		if len(self.stack) == 0 :
			return True
		return False
	def isfull(self) :
		#判断栈满
		if len(self.stack) == self.size :
			return True
		return False

#后序遍历以得到逆波兰表达式
def post_order(tree,res):
	if tree == None:
		return
	post_order(tree.l,res)
	post_order(tree.r,res)
	res.append(tree.data)

#根据逆波兰表达式求答案
def result(res):
	s=Stack(20)
	s.push(res[0])
	i=1
	r=0
	while(not s.isempty()):
		print(s)
		if res[i]<='9' and res[i]>='0':
			s.push(res[i])
		else:
			y = int(s.pop())
			x = int(s.pop())
			if res[i]=='+' :
				r = x+y
			elif res[i]=='-' :
				r = x-y
			elif res[i]=='*':
				r = x*y
			else:
				r = x/y
			s.push(r)
		if i==len(res)-1 :
			return s.pop()
		i=i+1

if __name__ == '__main__':
	a="4+3-1+5/3+6*2"
	b=BuildTree(a)
	l=b.build(a)
	res=list("")
	post_order(l,res)#得到的res结果就是：['4', '3', '+', '1', '-', '5', '3', '/', '+', '6', '2', '*', '+']
	print(res)
	print(result(res))
