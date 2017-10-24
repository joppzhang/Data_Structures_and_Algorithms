#*_*coding:utf-8*_*

#树的节点
class AvlNode(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#构建树的操作
class createAvlTree(object):
    def __init__(self):
        self.root = AvlNode(0)

    def deepth(self,root):
        if self==None:
            return 0
        elif self.left==None and self.right==None:
            return 1
        l = self.deepth(self.left)
        r = self.deepth(self.right)
        if l > r : 
            return l+1
        return r+1
        

    def search(self,value):
        r=self.root
        while (r != None):
            hot = r
            if r.data == value :
                return hot
            elif r.data > value :
                r = r.left
            else:
                r = r.right
            if r == None :
                return hot

    def insert(self,data):
        if self.root==None:
            self.root==AvlNode(data)
        else :
            i = AvlNode(data)
            key = self.search(data)
            if key.data > data:
                key.left = i
            else :
                key.right = i
        
        
#中序遍历方法
def tinTree(b,res):
    if b==None :
        return None
    tinTree(b.left,res)
    res.append(b.data)
    tinTree(b.right,res)

#Test
if __name__ == '__main__':
    t=createAvlTree()
    t.insert(3)
    t.insert(4)
    t.insert(1)
    t.insert(8)
    t.insert(2)
    res = list("")
    print(t.deepth(t.search(4)))
    tinTree(t.root,res)
    print(res)
