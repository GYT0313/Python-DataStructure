"""
File: linkedvertex.py
"""


class LinkedVertex(object):
    """顶点"""

    def __init__(self, label):
        self._label = label
        self._edge_list = list()
        self._mark = False

    def set_label(self, label, g):
        """修改顶点的标签"""
        # 弹出该顶点，重新设置label并加入字典
        g._vertices.pop(self._label, None)
        g._vertices[label] = self
        self._label = label

    def neighboring_vertices(self):
        """返回与顶点连通的其他顶点"""
        vertices = lsit()
        for edge in self._edge_list:
            vertices.append(edge.get_other_vertex(self))
        return iter(vertices)

    def remove_edge_to(self, to_vertex):
        """删除指定顶点的边"""
        edge = LinkedEdge(self, to_vertex)
        if edge in self._edge_list:
            self._edge_list.remove(edge)
            return True
        else:
            return False



