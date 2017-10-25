# coding=utf-8
# AVL树的Python实现(树的节点中包含了指向父节点的指针)


def get_height(node):
    return node.height if node else -1


def get_maximum(node):
    temp_node = node
    while temp_node.right:
        temp_node = temp_node.right
    return temp_node


def get_minimum(node):
    temp_node = node
    while temp_node.left:
        temp_node = temp_node.left
    return temp_node


def preorder_tree_walk(node):
    if node:
        print( node.key, node.height)
        preorder_tree_walk(node.left)
        preorder_tree_walk(node.right)


def left_left_rotate(tree, node):
    # 先将 node 和 node_left 之间及其左右节点赋值 (node_left.left node.right 保持不变)
    node_left = node.left
    node.left = node_left.right
    node_left.right = node
    if not node.p:
        tree.root = node_left
        node_left.p = None
    elif node == node.p.left:
        node.p.left = node_left
        node_left.p = node.p
    elif node == node.p.right:
        node.p.right = node_left
        node_left.p = node.p
    node.p = node_left
    while node:
        node.height = max(get_height(node.left), get_height(node.right)) + 1
        node = node.p


def right_right_rotate(tree, node):
    node_right = node.right
    node.right = node_right.left
    node_right.left = node
    if not node.p:
        tree.root = node_right
        node_right.p = None
    elif node == node.p.left:
        node.p.left = node_right
        node_right.p = node.p
    elif node == node.p.right:
        node.p.right = node_right
        node_right.p = node.p
    node.p = node_right
    while node:
        node.height = max(get_height(node.left), get_height(node.right)) + 1
        node = node.p


def left_right_rotate(tree, node):
    right_right_rotate(tree, node.left)
    left_left_rotate(tree, node)


def right_left_rotate(tree, node):
    left_left_rotate(tree, node.right)
    right_right_rotate(tree, node)


class AVLTreeNode(object):
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None
        self.height = 0


class AVLTree(object):
    def __init__(self):
        self.root = None

    def search(self, key):
        if not self.root:
            return None
        else:
            return self._search(key)

    def _search(self, key):
        start = self.root
        while start:
            if key < start.key:
                start = start.left
            elif key > start.key:
                start = start.right
            else:
                return start
        return None

    def insert(self, node):
        temp_root = self.root
        temp_node = None
        # 找到要插入的父节点(temp_node)
        while temp_root:
            temp_node = temp_root
            if node.key < temp_node.key:
                temp_root = temp_root.left
            elif node.key > temp_node.key:
                temp_root = temp_root.right
            else:
                raise (KeyError, "Error!")

        # 如果父节点为空 则说明这是一个空树 把 root 赋值即可
        if not temp_node:
            self.root = node
        elif node.key < temp_node.key:
            temp_node.left = node
            node.p = temp_node
            temp_node.height = max(get_height(temp_node.left), get_height(temp_node.right)) + 1
            temp_p = temp_node.p
            while temp_p:
                temp_p.height = max(get_height(temp_p.left), get_height(temp_p.right)) + 1
                temp_p = temp_p.p
        elif node.key > temp_node.key:
            temp_node.right = node
            node.p = temp_node
            temp_node.height = max(get_height(temp_node.left), get_height(temp_node.right)) + 1
            temp_p = temp_node.p
            while temp_p:
                temp_p.height = max(get_height(temp_p.left), get_height(temp_p.right)) + 1
                temp_p = temp_p.p
        self.fixup(node)

    def fixup(self, node):
        if node == self.root:
            return
        while node:
            if get_height(node.left) - get_height(node.right) == 2:
                if node.left.left:
                    left_left_rotate(self, node)
                else:
                    left_right_rotate(self, node)
                break
            elif get_height(node.right) - get_height(node.left) == 2:
                if node.right.right:
                    right_right_rotate(self, node)
                else:
                    right_left_rotate(self, node)
                break
            node = node.p

    def delete(self, key):
        temp_node = self.root
        while temp_node:
            if key > temp_node.key:
                temp_node = temp_node.right
            elif key < temp_node.key:
                temp_node = temp_node.left
            else:
                break
        if not temp_node:
            return False
        elif temp_node.left and temp_node.right:
            if get_height(temp_node.left) > get_height(temp_node.right):
                # 注意删除的时候不是直接把左右子树往上提 而是分别找到左右子树中的最大值和最小值往上提
                # 由于是最大子节点 故一定没有右子
                node_max = get_maximum(temp_node.left)
                if node_max.left:
                    node_max_p = node_max.p
                    node_max_p.right = node_max.left
                    node_max.left.p = node_max_p
                node_max.right = temp_node.right
                temp_node.right.p = node_max
                node_max.left = temp_node.left
                temp_node.left.p = node_max
                if temp_node.p:
                    if temp_node == temp_node.p.left:
                        temp_node.p.left = node_max
                        node_max.p = temp_node.p
                    else:
                        temp_node.p.right = node_max
                        node_max.p = temp_node.p
                else:
                    self.root = node_max
                    node_max.p = None
                temp_node = node_max
            else:
                node_min = get_minimum(temp_node.right)
                if node_min.right:
                    node_min_p = node_min.p
                    node_min_p.left = node_min.right
                    node_min.right.p = node_min_p
                node_min.left = temp_node.left
                temp_node.left.p = node_min
                node_min.right = temp_node.right
                temp_node.right.p = node_min
                if temp_node.p:
                    if temp_node == temp_node.p.left:
                        temp_node.p.left = node_min
                        node_min.p = temp_node.p
                    else:
                        temp_node.p.right = node_min
                        node_min.p = temp_node.p
                else:
                    self.root = node_min
                    node_min.p = None
                temp_node = node_min
        temp_node.height = max(get_height(temp_node.left), get_height(temp_node.right)) + 1
        self.fixup(temp_node)


def main():
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = AVLTree()
    for number in number_list:
        node = AVLTreeNode(number)
        tree.insert(node)
    preorder_tree_walk(tree.root)
    tree.delete(4)
    print ('==========')
    preorder_tree_walk(tree.root)


if __name__ == '__main__':
    main()