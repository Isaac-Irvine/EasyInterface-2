
class Variable:
    def __init__(self, name, value=None, comment=None):
        self._name = name
        self._comment = comment
        self._value = value
        self._listeners = set()

    def set_value(self, value):
        self._value = value
        for listener in self._listeners:
            listener.run()

    def get_value(self):
        return self._value

    def add_listener(self, listener):
        self._listeners.add(listener)

    def set_comment(self, comment):
        self._comment = comment

    def get_comment(self):
        return self._comment

    def get_name(self):
        return self._name


class Integer(Variable):
    def __init__(self, *args, **kwargs):
        if "value" not in kwargs:
            kwargs["value"] = 0
        super().__init__(*args, **kwargs)


class Float(Variable):
    def __init__(self, *args, **kwargs):
        if "value" not in kwargs:
            kwargs["value"] = 0.0
        super().__init__(*args, **kwargs)


class String(Variable):
    def __init__(self, *args, **kwargs):
        if "value" not in kwargs:
            kwargs["value"] = ""
        super().__init__(*args, **kwargs)
