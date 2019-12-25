
class BadSaveException(Exception):
    """
    Gets raised whenever a save files fails to load because of a corrupt save. i.e. there are bits missing
    """
    pass
