"""
File: model.py
定义PFEvaluatorModel 和 PFEvaluator
示例：
In [1]: from model import PFEvaluatorModel

In [2]: pfe = PFEvaluatorModel()

In [3]: pfe.evaluate("20 2 + 11 / 5 * 9 -")
Out[3]: 1

In [4]: pfe.evaluate("20 2 +")
Out[4]: 22

In [5]: pfe.evaluate("20 2 + 11 /")
Out[5]: 2

In [6]: pfe.evaluate("20 2 + 11 / 5 *")
Out[6]: 10

In [7]: pfe.evaluate("20 2 + 11 / 5 * 9 -")
Out[7]: 1
"""

from tokens import Token
from scanner import Scanner
from arraystack import ArrayStack

class PFEvaluatorModel(object):

    def evaluate(self, source_str):
        """计算值"""
        self._evaluator = PFEvaluator(Scanner(source_str))
        value = self._evaluator.evaluate()
        return value

    def format(self, source_str):
        """格式化"""
        normalized_str = ""
        scanner = Scanner(source_str)
        while scanner.has_next():
            normalized_str += str(scanner.next()) + " "
        return normalized_str


class PFEvaluator(object):
    
    def __init__(self, scanner):
        self._expression_so_far = ""
        self._operand_stack = ArrayStack()
        self._scanner = scanner

    def evaluate(self):
        while self._scanner.has_next():
            current_token = self._scanner.next()
            self._expression_so_far += str(current_token) + " "
            if current_token.get_type() == Token.INT:   # 数字入栈
                self._operand_stack.push(current_token)
            elif current_token.is_operator():   # 操作符计算
                if len(self._operand_stack) < 2:    # 栈内数字小于2
                    raise AttributeError (\
                        "Too few operands on the stack")
                t2 = self._operand_stack.pop()
                t1 = self._operand_stack.pop()
                result = \
                        Token(self._compute_value(current_token,
                                                    t1.get_value(),
                                                    t2.get_value()))
                self._operand_stack.push(result)
            else:
                raise AttributeError("Unknown token type")
        if len(self._operand_stack) > 1: # 计算完成后, 栈内深入数字大于2
            raise AttributeError(\
                "Too many operands on the stack")
        result = self._operand_stack.pop()
        return result.get_value()
        
    def __str__(self):
        result = "\n"
        if self._expression_so_far == "":
            result += \
                "Portion of expression processed none\n"
        else:
            result += "Portion of expression processed: " + \
                self._expression_so_far + "\n"
        if self._operand_stack.isEmpty():
            result += "Thre stack is empty"
        else:
            result += "Operands on the stack: " + \
                str(self._operand_stack)
        return result

    def _compute_value(self, op, value1, value2):
        result = 0
        the_type = op.get_type()
        if the_type == Token.PLUS:
            result = value1 + value2
        elif the_type == Token.MINUS:
            result = value1 - value2
        elif the_type == Token.MUL:
            result = value1 * value2
        elif the_type == Token.DIV:
            result = value1 // value2
        else:
            raise AttributeError("Unknown operator")
        return result
