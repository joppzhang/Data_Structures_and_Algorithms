# *_*coding:utf-8*_*
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


#Test
s = Stack(10)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.pop())
print(s.pop())
print(s.pop())


