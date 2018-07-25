from random import random
from module.getOptions import findItm

def decision(onSwitch = None, offSwitch = None, numChance = None, capChance = None):
    if onSwitch is None:
        onSwitch = ["ALLON"]
    if offSwitch is None:
        offSwitch = ["ALLOFF"]

    def _item(i):
        # if bool, take as is
        # if str use getOptions
        # if None then None
        if (type(i) == bool) or (i is None):
            return i
        elif type(i) == str:
            return findItm(item = i)
        else:
            return None

    def _list(_input):
        items = []

        # if list then
        ## for all items in list check items
        ## otherwise check single item
        if type(_input) == list:
            for _in in _input:
                items.append(_item(i = _in))
        else:
            items.append(_item(_input))

        return items

    on = _list(_input = onSwitch)
    off = _list(_input = offSwitch)

    if any(off):
        return False
    elif any(on):
        return True
    elif (numChance is None) or (numChance - capChance == 0):
        return True
    else:
        random() <= 1 / (numChance - capChance)