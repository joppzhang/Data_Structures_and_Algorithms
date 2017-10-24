#*_*coding = utf-8*_*

#二叉搜索树

#二叉树节点，这里我们以data就是key，不考虑有重复元素
class BstNode(object):
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

#二叉树的操作
class BstTree(object):
    def __init__(self,data):
        self.root = BstNode(data)

    #查找返回值是节点对象，这样方便下面的插入操作。
    #如果返回存在，就返回本身，和True
    #否则返回最后一个叶子和False
    def search(self,value):
        r=self.root
        while (r != None):
            hot = r
            if r.data == value :
                return hot,True
            elif r.data > value :
                r = r.left
            else:
                r = r.right
            if r == None :
                return hot,False

    def insert(self,value):
        i = BstNode(value)
        x,f=self.search(value)
        if x.data > value :
            x.left = i
        else :
            x.right = i

    #def delete(self,value):

#中序遍历方法，可以得到排序后的结果
def tinTree(b,res):
    if b==None :
        return None
    tinTree(b.left,res)
    res.append(b.data)
    tinTree(b.right,res)

#主方法Test
if __name__ == '__main__':
    b=BstTree(8)
    b.insert(2)
    b.insert(3)
    b.insert(5)
    b.insert(7)
    b.insert(9)
    b.insert(1)
    b.insert(4)
    b.insert(6)
    print(b.search(5))
    print(b.search(0))
    res = list("")
    tinTree(b.root,res)
    print(res)
