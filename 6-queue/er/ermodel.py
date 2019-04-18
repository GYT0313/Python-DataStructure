"""
File: ermodel.py
"""

from linkedpriorityqueue import LinkedPriorityQueue


class Condition(object):
    """三个病情状态 1 2 3"""

    def __init__(self, rank):
        self._rank = rank

    def __eq__(self, other):
        return self._rank == other._rank

    def __lt__(self, other):
        return self._rank < other._rank

    def __le__(self, other):
        return self._rank <= other._rank

    def __str__(self):
        if self._rank == 1: return "critical"
        elif self._rank == 2:   return "serious"
        else:   return "fair"


class Patient(object):
    """病人对象, 包含名称、病情程度"""

    def __init__(self, name, condition):
        self._name = name
        self._condition = condition

    def __eq__(self, other):
        return self._condition == other._condition

    def __lt__(self, other):
        return self._condition < other._condition

    def __le__(self, other):
        return self._condition <= other._condition

    def __str__(self):
        return self._name + " / " + str(self._condition)


class ERModel(object):
    """模型调度器"""
    def __init__(self):
        self._patients_queue = LinkedPriorityQueue()

    def isEmpty(self):
        return self._patients_queue.isEmpty()

    def schedule(self, patient):
        """增加一个病人"""
        self._patients_queue.add(patient)

    def treat_next(self):
        """删除队头节点"""
        return self._patients_queue.pop()
