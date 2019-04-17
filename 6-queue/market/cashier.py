"""
File:cashier.py
"""


from linkedqueue import LinkedQueue

class Cashier(object):
    def __init__(self):
        self._total_customer_wait_time = 0
        self._customers_served = 0
        self._current_customer = None
        self._queue = LinkedQueue()

    def add_customer(self, c):
        self._queue.add(c)

    def serve_customers(self, current_time):
        # 1. 当前顾客不存在,
        if self._current_customer == None:
            # 等待队列为空, 直接返回
            if self._queue.isEmpty():
                return 
            else: # 不为空, 将队头顾客提升为当前顾客
                self._current_customer = self._queue.pop()
                # 等待总时间加上当前顾客等待的时间
                self._total_customer_wait_time += \
                    current_time - \
                    self._current_customer.arrival_time()
                self._customers_served += 1

        # 2. 给当前顾客一个单位服务
        self._current_customer.serve()

        # 如果当前顾客需要的单位服务已经满足, 则将当前顾客赋值为 None
        if self._current_customer.amount_of_service_needed() == 0:
            self._current_customer = None

    def __str__(self):
        """
        Returns my results: my total customers served,
        my average wait time per customer, and customers left on my queue.
        """
        result = "TOTALS FOR THE CASHIER\n" + \
                 "Number of customers served:        " + \
                 str(self._customers_served) + "\n"
        if self._customers_served != 0:
            ave_wait_time = self._total_customer_wait_time /\
                          self._customers_served
            result += "Number of customers left in queue: " + \
                      str(len(self._queue)) + "\n" + \
                      "Average time customers spend\n" + \
                      "waiting to be served:              " + \
                      "%5.2f" % ave_wait_time
        return result
