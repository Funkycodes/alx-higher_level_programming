def lookup(obj):
    """return available methods and variables of an object

    Args:
        obj (object): input object

    Returns:
        list: list of object methods and variables
    """
    return dir(obj)
