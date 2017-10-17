# *_*coding:utf-8*_*
# 构建队列以便下面层遍历使用
class MyQueue(object):
	def __init__(self,size):
		self.size = size
		self.queue=[]
	
	def push(self,num):
		if self.isfull():
			raise Exception("queue is full")
		self.queue.append(num)

	def pop(self):
		if self.isempty():
			raise Exception("queue is empty")
		firstelement = self.queue[0]
		self.queue.remove(firstelement)
		return firstelement

	def isempty(self):
		if len(self.queue)==0:
			return True
		return False

	def isfull(self):
		if len(self.queue)==self.size:
			return True
		return False
#二叉树结点
class BinTreeNode(object):
	def __init__(self,data):
		self.data = data
		self.l = None
		self.r = None
#重建二叉树
class RBT(object):
	def __init__(self,pre,tin):
		self.pre = pre
		self.tin=tin
	def rebuildTree(self,pre,tin):
		if len(pre)==0:
			return None
		if len(pre)==1:
			return BinTreeNode(pre[0])
		res = BinTreeNode(pre[0])
		res.l = self.rebuildTree(pre[1: tin.index(pre[0]) + 1], tin[: tin.index(pre[0])])
		res.r = self.rebuildTree(pre[tin.index(pre[0]) + 1: ], tin[tin.index(pre[0]) + 1: ])
		return res
#层遍历重建的二叉树
def travel(res):
	queue = MyQueue(10)
	queue.push(res)
	while queue.isempty()==False:
		temp = queue.pop()
		print(temp.data)
		if temp.l != None :
			queue.push(temp.l)
		if temp.r != None :
			queue.push(temp.r)

#主函数
if __name__ == '__main__':
	pre=[1,2,4,7,3,5,6,8]
	tin=[4,7,2,1,5,3,8,6]
	rbt = RBT(pre,tin)
	res = rbt.rebuildTree(pre,tin)
	travel(res)



