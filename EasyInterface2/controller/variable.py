
class Variable:
    """
    Used to store a piece of information.
    """

    def __init__(self, name, variable_type, value=None, comment=None):
        """

        :param name: Name of the variable
        :param variable_type: The type of variable. This can not be changed after creation
        :param value: The initial value of the variable
        :param comment: A comment that descries what the variable is
        """
        self._name = name
        self._type = variable_type
        self._comment = comment
        self._value = value
        self._actions = set()

    def add_listener(self, action):
        """
        When the value of the variable is changed, it will run the given action
        :param action: The action to run when the variable is changed
        :return: None
        """
        self._actions.add(action)

    def set_value(self, value):
        self._value = value
        for action in self._actions:
            action.run()

    def get_value(self):
        return self._value

    def set_comment(self, comment):
        self._comment = comment

    def get_comment(self):
        return self._comment

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_jsonable(self):
        """
        Gets all the information needed to recreate this Variable in JSON compatible data type
        :return: A dictionary with everything needed to recreate this Variable
        """
        # action add them self's when loaded
        return {
            'name': self._name,
            'type': self._type,
            'comment': self._comment,
            'value': self._value
        }
