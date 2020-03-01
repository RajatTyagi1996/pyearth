"""
Basic Functions to help
"""


def match(name1, name2, ltype):
    """
    param: name1
    param: name2
    param: lookuptype type
    returns: Boolean value
    """
    if ltype == "exact":
        return name1 == name2
    elif ltype == "iexact":
        return name1.lower() == name2.lower()
    elif ltype == "contains":
        return name2 in name1
    elif ltype == "icontains":
        return name2.lower() in name1.lower()
    else:
        return eval("name1.{0}(name2)".format(ltype))
