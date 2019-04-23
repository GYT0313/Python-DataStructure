"""
File: linkededge.py
"""


class LinkedEdge(object):

    def __init__(self, from_vertex, to_vertex, weight=None):
        self._vertex1 = from_vertex
        self._vertex2 = to_vertex
        self._weight = weight
        self._mark = False

    def __eq__(self, other):
        """比较"""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._vertex1 == other._vertex1 and \
                self._vertex1 == other._vertex2 and \
                self._weight == other._weight