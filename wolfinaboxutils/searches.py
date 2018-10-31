#========================================================#
# File:   Searches - Various search functions
# Author: wolfinabox
# GitHub: https://github.com/wolfinabox/pyutils
#========================================================#
from typing import Union

def rec_in(item,container:Union[list,tuple])->bool:
    """
    Recursively determine if a given item is in a list of lists (of lists etc...)\n
    <item> : The value to search for\n
    <container> : The list to search in\n
    return : True/Fals, if the item was found
    """
    #Check if container is not an actual container
    if not type(container) in (list,tuple):
        return False
    #Check if the item is in the current container
    if item in container:
        return True
    #Recursively go through every container in the current container
    contains=False
    for i in container:
            contains= rec_in(item,i)
    return contains

def rec_dict_get(key,container:Union[list,tuple,dict],always_list:bool=False):
    """
    Recursively get the value(s) associated with a key from a container of dictionaries\n
    <key> : The key to search for\n
    <container> : The container to search in\n
    <always_list> : Return a list even if only one item was found. Default: False\n
    return : The value found, a list of all values found if more than one (or always_list==True), or None if not found
    """
    #Check if the container is a dict
    if type(container) is dict:
        return container[key] if key in container else None
    #Check if the container is not actually a container
    if not type(container) in (list,tuple):
        return None
    #Recursively go through every container in the current container
    items=[]
    for i in container:
        if type(container) in (list,tuple,dict):
            res=rec_dict_get(key,i,always_list)
            if res:
                if type(res) in (list,tuple):
                    items+=list(res)
                else: items.append(res)
    if not items: return False
    if len(items)==1 and not always_list: return items[0]
    return items

def any_in(a:Union[list,tuple,dict], b:Union[list,tuple,dict])->bool:
    """
    Check if any elements from set a are in set b\n
    <a>    : The first set\n
    <b>    : The second set\n
    returns: True/False, whether or not any elements from set a are in set b
    """
    return not set(a).isdisjoint(b)