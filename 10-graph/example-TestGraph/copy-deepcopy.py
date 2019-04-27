"""
File: algorithms.py
"""

from linkedstack import LinkedStack
import copy
import sys


def topo_sort(g, start_label=None):
    stack = LinkedStack()
    g.clear_vertex_marks()
    for v in g.vertices():
        if not v.is_marked():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack):
    """深度优先搜索算法"""
    v.set_mark()
    for w in g.neighboring_vertices(v.get_label()):
        if not w.is_marked():
            dfs(g, w, stack)
    stack.push(v)


def span_tree(g, start_label):
    """最小生成树"""
    sys.setrecursionlimit(1000)  # set the maximum depth as 1500
    best_paths = []
    min_weights = 99999

    def recurse(w, stack):
        if not w.is_marked():
            # 顶点未标记则入栈
            stack.push(w)
            w.set_mark()
            for x in w.neighboring_vertices():
                # 继续从顶点的连通节点往下继续遍历
                recurse(x, stack)
                if stack.get_size() != g.size_vertices():
                    stack.pop()
                    x.clear_mark()
                    return None
                else: # 递归回流时计算权重值
                    edge = g.get_edge(w.get_label(), x.get_label())
                    stack.add_weights(edge.get_weight())
                    # best_paths.append(stack)
                    # sun_stack = copy.deepcopy(stack)
                    # m = sun_stack.pop()
                    # m.clear_mark()
                    # stack = sun_stack
            # m = stack.pop()
            # m.clear_mark()
        else:
            return None

    for v in g.vertices():
        g.clear_vertex_marks()
        g.clear_edge_marks()
        # stack存储整个顶点, sun_stack复制stack的最新状态并继续遍历
        stack = LinkedStack()
        stack.push(v)
        v.set_mark()
        sun_stack = copy.deepcopy(stack)
        for w in v.neighboring_vertices():
            # 递归遍历
            recurse(w, sun_stack)
            # 如果遍历结束,栈内顶点数==图的顶点数代表该次遍历成功，加入成功列表
            if sun_stack.get_size() == g.size_vertices():
                edge = g.get_edge(v.get_label(), w.get_label())
                sun_stack.add_weights(edge.get_weight())
                if sun_stack.get_weights() < min_weights:
                    best_paths.clear()
                    best_paths.append(sun_stack)
                elif sun_stack.get_weights() == min_weights:
                    best_paths.append(sun_stack)
                sun_stack = copy.deepcopy(stack)
            else: # 不成功则出栈，继续下一个连接顶点的遍历
                w.clear_mark()
        if len(best_paths) > 0:
            print(best_paths[0], best_paths[0].get_weights())

    if best_paths == None:
        return "No best path"
    results = ""
    results += "Here has " + str(len(best_paths)) + " paths:\n"
    for path_stack in best_paths:
        temp = ""
        for v in path_stack:
            temp = "->" + v.get_label() + temp
        temp = temp[2:]
        results += temp + "\n"
    return results





def shortest_paths(g, start_label):
    """dijkstra"""
    pass
