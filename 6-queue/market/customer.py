"""
File: customer.py
"""

import random

class Customer(object):

    # 类方法
    @classmethod
    def generate_customer(cls, probability_of_new_arrival,
                        arrival_time,
                        average_time_per_customer):

        """
            在满足随机数的条件下返回customer 对象, 否则返回 None
        """
        if random.random() <= probability_of_new_arrival:
            return Customer(arrival_time, average_time_per_customer)
        else:
            return None

    def __init__(self, arrival_time, service_needed):
        self._arrival_time = arrival_time
        self._amount_of_service_needed = service_needed

    def arrival_time(self):
        return self._arrival_time

    def amount_of_service_needed(self):
        return self._amount_of_service_needed

    def serve(self):
        """需要的单位服务数-1"""
        self._amount_of_service_needed -= 1
