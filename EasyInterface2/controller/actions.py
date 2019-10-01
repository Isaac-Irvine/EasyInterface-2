

class Action:
    def __init__(self):
        self._comment = ""

    def run(self):
        pass

    def set_comment(self, comment):
        self._comment = comment

    def get_comment(self):
        return self._comment


class ActionList:
    def __init__(self):
        self._actions = []
        self._comment = ""

    def run(self):
        for action in self._actions:
            action.run()

    def set_comment(self, comment):
        self._comment = comment

    def get_comment(self):
        return self._comment
