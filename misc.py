#========================================================#
# File:   Misc - Various miscellaneous functions
# Author: wolfinabox
# GitHub: https://github.com/wolfinabox/pyutils
#========================================================#
def function_call_str(func,*args,**kwargs)->tuple:
    """
    Return a string representing the function call\n
    <func>    : The function\n
    <*args>   : The arguments to pass to the function\n
    <**kwargs>: \n
    \t<equals>: 'Whether or not to print the = return_value string' (in case you want to format it yourself)\n
    return    : A tuple containing the function call string, and the return value\n
    EG: function_call_str(add,2,4) = ('function_call_str(add,2,4)',6)
    """
    return_val=func(*args)
    arg_strs=', '.join([("'"+arg+"'" if isinstance(arg,str) else str(arg)) for c,arg in enumerate(args)])
    f_str=str(func.__name__)+'('+arg_strs+')'+(' = '+str(return_val) if ('equals' in kwargs and kwargs['equals']) else '')
    return (f_str,return_val)

def is_int(s:str)->bool:
    try: 
        int(s)
        return True
    except ValueError:
        return False

def is_float(s:str)->bool:
    try: 
        float(s)
        return True
    except ValueError:
        return False

def askYN(question:str,default='')->bool:
    """
    Asks the user a yes/no question until a valid input is given.\n
    <question> : The question to ask\n
    <default>  : A default option to give
    """
    default=default.strip().lower()
    response='0'
    qText=(question+(' ['+default.lower().strip()+']') if default and default[0] in ('y','n') else question)+': '
    while response[0] not in ('y','n'):
        response=input(qText).strip().lower()
        if not response or response.isspace():
                response=default if default in ('y','n') else '0'

    return response[0]=='y'