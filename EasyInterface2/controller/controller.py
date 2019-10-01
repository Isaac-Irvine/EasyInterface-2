

class Controller:
    def __init__(self):
        self._variables = {}
        self._functions = {}

    def add_function(self, name, function):
        if name in self._functions:
            raise ValueError("this name already exists in functions")
        self._functions[name] = function
