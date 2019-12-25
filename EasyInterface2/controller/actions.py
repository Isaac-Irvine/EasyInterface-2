
class Action:
    """
    To be used as a super class for all actions
    """

    def __init__(self, name):
        self._name = name
        self._comment = ""

    def run(self):
        """
        Execute the action.
        Should be overridden by subclasses
        :return: None
        """
        pass

    def set_comment(self, comment):
        self._comment = comment

    def get_comment(self):
        return self._comment

    def get_name(self):
        return self._name


class ActionList(Action):
    """
    Stores a list of actions that when ran, will run all the actions in the list in order
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._actions = []

    def run(self):
        for action in self._actions:
            action.run()
