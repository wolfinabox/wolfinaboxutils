#========================================================#
# File:   Test - A file demonstrating the use of all my functions
# Author: wolfinabox
# GitHub: https://github.com/wolfinabox/pyutils
#========================================================#
from wolfinaboxutils.formatting import *
from wolfinaboxutils.misc import *
from wolfinaboxutils.searches import *
from wolfinaboxutils.system import *

#SEARCHES
print('Searches:')
#List Search
l1=[1,[2,(3,(4,'hello'))]]
print(function_call_str(rec_in,'hello',l1,equals=True)[0])

#Dict Search
d1=[([({'hello':'world'},15),28],['asdf'])]
print(function_call_str(rec_dict_get,'hello',d1,equals=True)[0])

#Any In
s1=[1,2,3,4]
s2=[4,5,6,7]
s3=[5,6,7]
print(function_call_str(any_in,s1,s2,equals=True)[0])
print(function_call_str(any_in,s1,s3,equals=True)[0])

#Flatten
ll1=[1,2,(3,4,[5,6],(7,8)),9,10]
print(function_call_str(flatten,ll1,equals=True)[0])

#FORMATTING
print('\nFormatting')
#Truncate
s1='This string is longer than 25 characters'
print(function_call_str(truncate,s1,25,'...',equals=True)[0])

#Truncate Words
print(function_call_str(truncate_words,s1,25,'...',equals=True)[0])

#System
print('\nSystem: ')
#Is executable?
print(function_call_str(is_executable,equals=True)[0])

#Script Directory
print(function_call_str(script_dir,equals=True)[0])

#Local File/Directory
print(function_call_str(local_path,'README.md',equals=True)[0])

#MISC
print('\nMisc:')
#Is Int?
print(function_call_str(is_int,'42',equals=True)[0])
print(function_call_str(is_int,'42.0042',equals=True)[0])

#Is Float
print(function_call_str(is_float,'42',equals=True)[0])
print(function_call_str(is_float,'42.0042',equals=True)[0])

#Ask Yes/No
print(function_call_str(askYN,'> Is 42 a good number?',equals=True)[0])