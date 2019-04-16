"""
File: scanner.py
A scanner for processing languages.
"""

from tokens import Token

class Scanner(object):

    EOE = ';'        # end-of-expression
    TAB = '\t'       # tab

    def __init__(self, source_str):
        self._source_str = source_str
        self._get_first_token()

    def has_next(self):
        return self._current_token != None

    def next(self):
        if not self.has_next():
            raise Exception("There are no more tokens")           
        temp = self._current_token
        self._get_next_token()
        return temp

    def _get_first_token(self):
        self._index = 0
        self._current_char = self._source_str[0]
        self._get_next_token()
    
    def _get_next_token(self):
        self._skip_white_space()
        if self._current_char.isdigit():
            self._current_token = Token(self._getInteger())
        elif self._current_char == Scanner.EOE:
            self._current_token = None
        else:
            self._current_token = Token(self._current_char)
            self._next_char()
    
    def _next_char(self):
        if self._index >= len(self._source_str) - 1:
            self._current_char = Scanner.EOE
        else:
            self._index += 1
            self._current_char = self._source_str[self._index]
    
    def _skip_white_space(self):
        while self._current_char in (' ', Scanner.TAB):
            self._next_char()
    
    def _getInteger(self):
        num = 0
        while True:
            num = num * 10 + int(self._current_char)
            self._next_char()
            if not self._current_char.isdigit():
                break
        return num


def main():
    # A simple tester program
    while True:
        source_str = input("Enter an expression: ")
        if source_str == "": break
        scanner = Scanner(source_str)
        while scanner.has_next():
            print(scanner.next())

if __name__ == '__main__': 
    main()

