"""
File: tokens.py
计算后缀表达式
"""

class Token(object):
    UNKNOWN = 0     # unknown
    INT = 4         # integer
    MINUS = 5       # -
    PLUS = 6        # +
    MUL = 7         # *
    DIV = 8         # /
    FIRST_OP = 5    # 第一个操作符

    def __init__(self, value):
        if type(value) == int:
            self._type = Token.INT
        else:
            self._type = self._make_type(value)
        self._value = value

    def is_operator(self):
        return self._type >= Token.FIRST_OP

    def __str__(self):
        return str(self._value)

    def get_type(self):
        return self._type

    def get_value(self):
        return self._value

    def _make_type(self, ch):
        if ch == '*': return Token.MUL
        elif ch == '/': return Token.DIV
        elif ch == '+': return Token.PLUS
        elif ch == '-': return Token.MINUS
        else: return Token.UNKNOWN

