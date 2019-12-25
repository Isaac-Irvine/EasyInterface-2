from .actions import ActionList


class Variable:
    """
    Used to store a piece of information.
    Information should never be None
    """

    def __init__(self, name, variable_type, value, comment=None, on_update_action=None):
        """

        :param name: Name of the variable
        :param variable_type: The type of variable. This can not be changed after creation
        :param value: The initial value of the variable
        :param comment: A comment that descries what the variable is
        """
        self._name = name
        self._type = variable_type
        self._comment = "" if comment is None else comment
        self._value = value
        self._on_update_action = ActionList() if on_update_action is None else on_update_action

    def set_value(self, value):
        self._value = value
        self._on_update_action.run()

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
            'value': self._value,
            'on_update_action': self._on_update_action.get_jsonable()
        }
