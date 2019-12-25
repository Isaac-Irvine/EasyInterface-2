

class Controller:
    def __init__(self):
        self._variables = set()
        self._actions = set()

    def add_action(self, action):
        if action.get_name() in [i.get_name() for i in self._actions]:
            raise ValueError('There is already an action with this name. Name: ' + action.get_name())
        self._actions.add(action)

    def add_variable(self, variable):
        if variable.get_name() in [i.get_name() for i in self._variables]:
            raise ValueError('There is already a variable with this name. Name: ' + variable.get_name())
        self._variables.add(variable)