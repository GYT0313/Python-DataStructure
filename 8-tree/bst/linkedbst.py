"""
File: linkedbst.py
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode


class LinkedBST(AbstractCollection):
    """基于链表的二叉搜索树"""

    def __init__(self, source_collection=None):
        self._root = None
        AbstractCollection.__init__(self, source_collection)


    def find(self, item):
        """搜索二叉树，返回item"""
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self._root)

    def __iter__(self):
        """前序遍历"""
        lyst = list()
        def recurse(node):
            if node != None:
                lyst.append(node.data)
                recurse(node.left)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def inorder(self):
        """中序遍历"""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """后序遍历"""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self._root)
        return iter(lyst)

    def levelorder(self):
        pass

    def __str__(self):
        """返回字符串，将原树逆时针旋转90度（变成了横向打印）"""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "|" * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self._root, 0)

    def add(self, item):
        """增加item 到对应的位置"""
        def recurse(node):
            # item < node.data
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # item >= node.data
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
        if self.isEmpty():
            self._root = BSTNode(item)
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """删除item"""
        if self.find(item) == None:
            raise KeyError("Item not in tree.")

        def lift_max_in_left_subtree_to_top(top):
            # 将被删除节点的左子节下的最大项替换被删除的节点
            # (即左子树最后边的节点)
            parent = top
            current_node = top.left
            # 找到左子树最大值的节点
            while current_node.right != None:
                parent = current_node
                current_node = current_node.right
            # 将最大值替换被删除的节点
            top.data = current_node.data
            if parent == top:
                top.left = current_node.left
            else: # 将最大值节点的左节点赋值给父节点的右节点
                parent.right = current_node.left

        if self.isEmpty():
            return None
        # 使用pre_root 作为新的临时根节点(因为可能删除的就是根节点)
        item_removed = None
        pre_root = BSTNode(None)
        pre_root.left = self._root
        parent = pre_root
        directioin = 'L'
        current_node = self._root
        while current_node != None:
            # 删除的就是根节点
            if current_node == item:
                item_removed = current_node.data
                break
            parent = current_node
            if item < current_node.data:
                directioin = 'L'
                current_node = current_node.left
            else:
                directioin = 'R'
                current_node = current_node.right
        # 树中没有item 节点
        if item_removed == None:
            return None
        # case1: 当前节点有左节点和右节点
        if current_node.left != None \
            and current_node.right != None:
            lift_max_in_left_subtree_to_top(current_node)
        else:
            # case2: 没有左节点
            if current_node.left == None:
                new_child = current_node.right
            # case3: 没有右节点
            else:
                new_child = current_node.left
            # case2 和 case3时
            if directioin == 'L':
                parent.left = new_child
            else:
                parent.right = new_child
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = pre_root.left
        return item_removed
