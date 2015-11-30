"""
    Use min/max to try to improve performance of unordered
    lists by having Fast-Fail for contains when possible.

    Keep unordered list with min in position[0] and max
    in position[1]. Helper methods ensure structure is
    maintained in the face of additions and remove requests.

    Contains method returns False immediately if not possible
    to be in the list, based on these values.

    Author: George Heineman    
"""

def minmax_add(mmlist, val):
    """Insert element val into mmlist."""
    if len(mmlist) == 0:
        mmlist.append(val)
        return
    
    if val < mmlist[0]:
        mmlist.insert(-1,mmlist[0])
        mmlist[0] = val
    elif val > mmlist[-1]:
        mmlist.append(val)
    else:
        mmlist.insert(-1, val)

def minmax_remove(mmlist, val):
    """Remove element from mmlist."""
    if len(mmlist) == 0:
        return
    if len(mmlist) <= 2:
        if val == mmlist[0]:
            del mmlist[0]
        elif val == mmlist[-1]:
            del mmlist[-1]
        return

    # have at least three elements.
    if val == mmlist[0]:
        newmin = 2
        for i in range(3,len(mmlist)):
            if mmlist[i] < mmlist[newmin]:
                newmin = i
        mmlist[0] = mmlist[newmin]
        del mmlist[newmin]
    elif val == mmlist[-1]:
        newmax = 2
        for i in range(3,len(mmlist)):
            if mmlist[i] > mmlist[newmax]:
                newmax = i
        mmlist[1] = mmlist[newmax]
        del mmlist[newmax]
    else:
        for i in range(1,len(mmlist)):
            if mmlist[i] == val:
                del mmlist[i]
                return
    
def minmax_contains(mmlist, val):
    """Determine whether mmlist contains val."""
    if len(mmlist) == 0:
        return False
    
    if val < mmlist[0] or val > mmlist[-1]:
        return False

    return val in mmlist

"""
Change Log:

"""
