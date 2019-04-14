"""
3.1
优化顺序搜索
对一个有序列表顺序搜索，当目标项比给定的元素要小时，就停止。
最好情况: O(1)
最坏情况: O(n)
平均: O(n)
"""
def sequential_search(lyst, target):
    if target < lyst[0]:
        return -1
    for index in range(0, len(lyst)):
        if lyst[index] == target:
            return index
    return -1


"""
3.2
实现列表的reverse方法
最好情况: O(n/2) ~ O(n)
最坏: O(n)
平均: O(n)
"""
def myself_reverse(lyst):
    for index in range(len(lyst) // 2):
        r_index = len(lyst) - 1 - index
        lyst[index], lyst[r_index] = lyst[r_index], lyst[index]


"""
3.3
pow 指数函数
"""
def expo(num, exp):
    if exp < 1:
        return 1
    return num * expo(num, exp - 1)



"""
3.5
选择排序: 允许指定升、降序排列
"""
def selection_sort(lyst, reverse=False):
    for i in range(len(lyst) - 1):
        for j in range(i + 1, len(lyst)):
            if reverse:
                if lyst[i] < lyst[j]:
                    lyst[i], lyst[j] = lyst[j], lyst[i]
            else:
                if lyst[i] > lyst[j]:
                    lyst[i], lyst[j] = lyst[j], lyst[i]


"""
3.6
修改Fibonacci函数，使用记忆技术，接收一个字典保存参数和值。
O(n)
"""
def fib_dic(n, dic, counter):
    if n < 3:
        return 1
    keys = dic.keys()
    key = "fib({})".format(n)
    if key not in keys:
        counter.count()
        dic[key] = fib_dic(n - 1, dic, counter) + fib_dic(n - 2, dic, counter)
    return dic[key]

"""
O(k^n)
"""
def fib(n, counter):
    if n < 3:
        return 1
    counter.count()
    return fib(n - 1, counter) + fib(n - 2, counter)

"""递归次数计数器"""
class Counter(object):
    """docstring for Counter"""
    def __init__(self):
        self._counter = 0
    
    def count(self):
        self._counter += 1























def main():
    print(sequential_search(list(range(0, 8)), -2))

if __name__ == '__main__':
    main()