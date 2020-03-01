"""
Basic Functions to help
"""
import os
from pandas import DataFrame

def match(name1, name2, ltype):
    """
    param: name1
    param: name2
    param: lookuptype type
    returns: Boolean value
    """
    if "/" in name1 or "\\" in name1:
        name1 = (os.path.split(name1)[-1]).split("?")[0]

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

def filter_list(flist, abspath):
    nlist = []
    for n in flist:
        if abspath:
            nlist.append(n)
        else:
            nlist.append(os.path.split(n)[-1])
    return nlist

