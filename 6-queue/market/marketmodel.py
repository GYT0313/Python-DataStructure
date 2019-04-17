"""
File: marketmodel.py
"""

from cashier import Cashier
from customer import Customer

class MarketModel(object):

    def __init__(self, length_of_simulation, average_time_per_cus,
                probability_of_new_arrival):
        self._probability_of_new_arrival = probability_of_new_arrival
        self._length_of_simulation = length_of_simulation
        self._average_time_per_cus = average_time_per_cus
        self._cashier = Cashier()

    def run_simulation(self):
        """运行时钟"""
        for current_time in range(self._length_of_simulation):
            # 1. 尝试生成一个customer
            customer = Customer.generate_customer(
                self._probability_of_new_arrival,
                current_time,
                self._average_time_per_cus)

            # 2. 发送顾客到收银员
            if customer != None:
                self._cashier.add_customer(customer)

            # 3. 告知收银员提供其他服务
            self._cashier.serve_customers(current_time)

    def __str__(self):
        return str(self._cashier)