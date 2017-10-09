#*_*coding:utf-8*_*

class liner_list(object):
	#初始化
	def __init__(self,maxSize):
		self.maxSize = maxSize
		#默认线性表是range(0,maxSize)
		self.data = list(range(0,maxSize))
		self.last = -1 #-1时候表示没有添加任何元素

	#获取线性表的长度，len(liner_list)
	def __len__(self):
		length = self.last+1
		return length

	#获取元素值
	def __getitem__(self,index):
		if self.isEmpty() :
			return None
		elif index < 1 or index > self.last +1:
			print("index out of range")
			return 
		else:
			return self.getElement(index)

	#设置元素值
	def __setitem__(self,index,value):
		if self.isEmpty():
			print("liner_list is empty")
			return
		elif index < 1 or index > self.last +1:
			print("index is out of range")
			return
		else:
			self.data[index-1]=value

	#获取元素,下表从 1 开始
	def getElement(self,index):
		return self.data[index-1]

	#删除元素
	def delElement(self,index):
		if self.isEmpty():
			print("liner_list is empty")
			return
		elif index < 1 or index > self.last +1:
			print("index is out of range")
			return
		else:
			for key in range(index,len(self)) :
				self.data[key-1]=self.data[key]
			self.last -= 1

	#添加元素
	def addElement(self,value):
		if self.isfull():
			print("the liner_list is full")
			return
		else:
			self.last += 1
			x=self.last
			self.data[x] = value

	#插入元素
	def insert(self,index,value):
		if self.isfull():
			print("liner_list is full")
			return
		elif index < 1 or index > self.last +1:
			print("index is out of range")
			return
		else:
			for key in range(self.last+1,index,-1):
				self.data[key]=self.data[key-1]
			self.data[index]=value
			self.last += 1
	

	#是否为空
	def isEmpty(self):
		if self.last ==-1:
			return True
		else:
			return False

	#获取索引
	def getIndex(self,value):
		if self.isEmpty():
			print ("liner_list is empty")
			return
		for key in range(0,self.last):
			if self.data[key]==value:
				return key+1

	#销毁列表
	def distory(self):
		self.last=-1

	#判断列表是否已经满
	def isfull(self):
		if (self.last+1) == self.maxSize:
			return True
		else:
			return False
