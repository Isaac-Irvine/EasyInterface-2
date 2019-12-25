from .saving_and_loading import BadSaveException

class Action:
    """
    To be used as a super class for all actions
    """

    _subclasses = {}  # Dictionary of all the subclasses of Action. Name as key, class as value.

    def __init_subclass__(cls, **kwargs):
        """
        When a subclass of Action is made, it is added to the list of subclasses
        :param kwargs: idk what this is used for. I just copied this off Stackoverflow
        :return: None
        """
        super().__init_subclass__(**kwargs)
        if cls.__name__ in Action._subclasses:
            raise RuntimeError('Subclass of that name already exists. Name: ' + cls.__name__)
        Action._subclasses[cls.__name__] = cls

    @staticmethod
    def get_subclass_of_name(name):
        """
        Gets the class with the given name
        :param name: Name of the class you want to find
        :return: The class if its found, ValueError if its not
        """
        return Action._subclasses[name]

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

    def get_jsonable(self):
        """
        Gets all the information needed to recreate this Action in JSON compatible data type.
        Most subclasses should add to this.
        :return: A dictionary with everything needed to recreate this Action
        """
        return {
            'name': self._name,
            'comment': self._comment,
            'type': type(self).__name__,
        }

    @staticmethod
    def from_jsonable(jsonable):
        """
        Makes a new instance of Action from the given JSON compatible data type
        :param jsonable: JSON compatible data type to load from
        :return: Action
        """
        # make sure all the keys are there
        for key in ['name', 'type', 'comment']:
            if key not in jsonable:
                raise BadSaveException('Action "' + key + '" key not found')

        # make sure a valid type is given
        if jsonable['type'] not in Action._subclasses:
            raise BadSaveException('No action named "' + jsonable['type'] + '" could be found')

        # initialise an instance of the class
        action = Action._subclasses[jsonable['type']](jsonable['name'])
        action.get_comment(jsonable['comment'])


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

    def get_jsonable(self):
        """
        Gets all the information needed to recreate this ActionList in JSON compatible data type.
        :return: A dictionary with everything needed to recreate this ActionList
        """
        jsonable = super().get_jsonable()
        jsonable['actions'] = [action.get_jsonable() for action in self._actions]
