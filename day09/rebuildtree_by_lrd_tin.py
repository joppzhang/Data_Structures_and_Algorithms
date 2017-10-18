# *_*coding:utf-8*_*
# 根据二叉树后序遍历结果和中序遍历结果重构二叉树
#后序遍历	|-------------------------------|--------------------------------|---------|
#			|----------左子树---------------|------------右子树--------------|--根节点-|
#			|-------------------------------|--------------------------------|---------|
#中序遍历
# 			|-------------------------------|---------|--------------------------------|
# 			|-----------左子树--------------|--根节点-|------------右子树--------------|
# 			|-------------------------------|---------|--------------------------------|
# 
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
	def __init__(self,lrd,tin):
		self.lrd = lrd
		self.tin=tin
	def rebuildTree(self,lrd,tin):
		if len(lrd)==0:
			return None
		if len(lrd)==1:
			return BinTreeNode(lrd[0])
		res = BinTreeNode(lrd[-1])
		res.l = self.rebuildTree(lrd[: tin.index(lrd[-1])], tin[:tin.index(lrd[-1])])
		res.r = self.rebuildTree(lrd[tin.index(lrd[-1]):-1], tin[tin.index(lrd[-1]) + 1: ])
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
	lrd=[7,4,2,5,8,6,3,1]
	tin=[4,7,2,1,5,3,8,6]
	rbt = RBT(lrd,tin)
	res = rbt.rebuildTree(lrd,tin)
	travel(res)



