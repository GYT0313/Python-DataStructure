"""
File: linkeddirectedgraph.py
"""


from abstractcollection import AbstractCollection

class LinkedDirectedGraph(AbstractCollection):

    def __init__(self, source_collection=None):
        slef._edge_count = 0
        self._vertices = dict()
        AbstractCollection.__init__(self, source_collection)

    def add_vertex(self, label):
        self._vertices[label] = LinkedVertex(label)
        self._size += 1

    def remove_vertex(self, label):
        """成功移除返回True"""
        removed_vertex = self._vertices.pop(label, None)
        if removed_vertex is None:
            return False

        # 删除其他顶点指向该顶点的边
        for vertex in self.vertices():
            if vertex.remove_edge_to(removed_vertex):
                self._edge_count -= 1

        # 删除该顶点指向其他顶点的边
        for edge in removed_vertex.incident_edges():
            self._edge_count -= 1

        # 顶点数量减一
        self._size -= 1
        return True

    def add_edge(self, from_label, to_label, weight):
        """添加一条带有权重的有向边"""
        from_vertex = self.get_vertex(from_label)
        to_vertex = self.get_vertex(to_label)
        from_vertex.add_edge_to(to_vertex, weight)
        self._edge_count += 1

    def get_edge(self, from_label, to_label):
        """获取一条边"""
        from_vertex = self.get_vertex(from_label)
        to_vertex = self.get_vertex(to_label)
        return from_vertex.get_edge_to(to_vertex)

    def remove_edge(self, from_label, to_label):
        from_vertex = self.get_vertex(from_label)
        to_vertex = self.get_vertex(to_label)
        edge_removed_flg = from_vertex.remove_edge_to(to_vertex)
        if edge_removed_flg:
            self._edge_count -= 1
        return edge_removed_flg

    def edges(self):
        """返回所有边的集合"""
        result = set()
        for vertex in self.vertices():
            edges = vertex.incident_edges()
            result = result.union(set(edges))
        return iter(result)


