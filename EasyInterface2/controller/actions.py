

class Action:
    """
    To be used as a super class for all actions
    """

    def __init__(self, name):
        self._name = name
        self._comment = ""
        self._listening_to = set()  # names of all the variables to listen too

    def run(self):
        pass

    def set_comment(self, comment):
        self._comment = comment

    def get_comment(self):
        return self._comment

    def get_name(self):
        return self._name

    def get_jsonable(self):
        """
        Gets all the information needed to recreate this Action in JSON compatible data type
        :return: A dictionary with everything needed to recreate this Action
        """
        return {
            'name': self._name,
            'comment': self._comment,
            'listening to': self._listening_to,
        }


class ActionList:
    """
    A list of actions that when ran, will run all the actions in the list in order
    """

    def __init__(self, name):
        self._actions = []
        self._name = name
        self._comment = ""
        self._listening_to = set()  # names of all the variables to listen too

    def run(self):
        for action in self._actions:
            action.run()

    def set_comment(self, comment):
        self._comment = comment

    def get_comment(self):
        return self._comment

    def get_name(self):
        return self._name

    def get_jsonable(self):
        """
        Gets all the information needed to recreate this ActionList in JSON compatible data type
        :return: A dictionary with everything needed to recreate this ActionList
        """
        return {
            'name': self._name,
            'comment': self._comment,
            'listening to': self._listening_to,
            'actions': [i.get_jsonable() for i in self._actions],
        }
