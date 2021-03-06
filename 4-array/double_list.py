"""
双向链表
实现：
1.链表的创建
2.节点的添加
3.节点删除
4.打印节点
"""


"""
链表结构的节点类
"""
class Node(object):
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.next = next
        self.previous = previous


class DoubleLink(object):
    """双向链表"""
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        if data != None:
            self.initialization(data)

    def initialization(self, data=None):
        """初始化"""
        if self.head != None:
            print("Erro: Link had been initialization!")
        elif data == None:
            print("Erro: Parameter data cannot be empty!")
        else:
            self._add_to_tail(data)

    def _add_to_tail(self, data):
        """增加节点"""
        if type(data) == int:
            data = [data]
        for da in data:
            node = Node(da)
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.tail = self.head
                while self.tail.next != None:
                    previous = self.tail
                    self.tail = self.tail.next
                    self.previous = previous
                # node节点前驱指向tail, 后继指向tail.next
                node.previous = self.tail
                node.next = self.tail.next
                # tail节点的后继指向node, 完成添加
                self.tail.next = node
                self.tail = self.tail.next

    def append(self, data=None):
        """向链表末尾添加节点"""
        self._add_to_tail(data)

    def travering(self):
        """打印所有节点"""
        if self.head == None:
            pass
        else:
            probe = self.head
            while probe != None:
                print(probe.data)
                probe = probe.next

    def length(self):
        """长度"""
        length = 0
        probe = self.head
        while probe != None:
            length += 1
            probe = probe.next
        return length

    def pop(self, index=None):
        """删除节点, 默认删除最后一个"""
        data = None
        if self.head == None:
            return data
        elif index != None and index <= 0:
            return "Erro: Parameter must be > 0!"
        elif index != None and index > self.length():
            return "Erro: Parameter must be " + \
                    "<= {}!".format(self.length())
        else:
            # 只有1个节点
            if self.head.next == None:
                data = self.head.data
                self.head = None
            else:
                if index == 1:    # 删除第一个节点
                    data = self.head.data
                    self.head = self.head.next
                    return data
                elif index == None:
                    index = self.length()
                probe = self.head
                i = 2   # 第一个节点之后
                while probe.next.next != None and i < index:
                    probe = probe.next
                    i += 1
                data = probe.next.data
                if index == self.length():    # 删除在尾部
                    probe.next = None
                else:   # 删除在中间
                    probe.next = probe.next.next
        return data

    def __str__(self):
        result = ""
        if self.head != None:
            probe = self.head
            while probe != None:
                result += str(probe.data) + "\n"
                probe = probe.next
        return result
