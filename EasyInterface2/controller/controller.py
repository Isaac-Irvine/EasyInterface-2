from .actions import Action
from .variable import Variable
from .saving_and_loading import BadSaveException

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

    def get_jsonable(self):
        """
        Gets all the information needed to recreate this Controller in JSON compatible data type
        :return: A dictionary with everything needed to recreate this Controller
        """
        return {
            'variables': [i.get_jsonable() for i in self._variables],
            'actions': [i.get_jsonable() for i in self._actions]
        }

    @classmethod
    def from_jsonable(cls, jsonable):
        """
        Makes a new instance of Controller from the given JSON compatible data type
        :param jsonable: JSON compatible data type to load from
        :return: Controller
        """
        controller = Controller()

        # make sure all the keys are there
        for key in ['variables', 'actions']:
            if key not in jsonable:
                raise BadSaveException('Controller "' + key + '" key not found')

        # must load variables before actions because actions looks for variables when being initialised
        for variable in jsonable['variables']:
            Variable.
            controller.add_variable()