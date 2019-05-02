#========================================================#
# File:   Format - Various string formatting functions
# Author: wolfinabox
# GitHub: https://github.com/wolfinabox/pyutils
#========================================================#
def truncate(data:str,length:int,append:str='')->str:
    """
    Truncates a string to the given length\n
    `data` The string to truncate\n
    `length` The length to truncate to\n
    `append` Text to append to the end of truncated string. Default: ''
    """
    return (data[:length]+append) if len(data)+len(append)>length else data

def truncate_words(data:str,length:int,append:str='')->str:
    """
    Truncates a string to the given length, rounded to the nearest whole word\n
    `data` The string to truncate\n
    `length` The length to truncate to\n
    `append` Text to append to the end of truncated string. Default: ''
    """
    if len(data)<=length: return data
    all_strs=data.split(' ')
    strs=[]
    i=0
    while len(' '.join(strs))+len(append)+len(all_strs[i])<=length:
        strs.append(all_strs[i])
        i+=1
    return ' '.join(strs)+append


def multi_split(delimiters:list, string:str, maxsplit:int=0,flags:int=0):
    """
    Split a string with multiple delimiters\n
    `delimiters` A list of delimiters to use (list of strs)\n
    `string` The string to split\n
    `maxsplit` The maximum number of times to split (the rest of the string becomes the last list item)\n
    `flags` Flags to pass in to `re.split()`
    """
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)
