#========================================================#
# File:   System - Various "system-related" functions
# Author: wolfinabox
# GitHub: https://github.com/wolfinabox/pyutils
#========================================================#
def is_executable()->bool:
    """
    Determine if the current script is packaged as an executable\n
    (EG: If packed into a .exe with PyInstaller)\n
    returns : True/False, if the script is an executable
    """
    import sys
    return getattr(sys,'frozen',False)

def script_dir()->str:
    """
    Get the path to the current script, whether running as an executable or in an interpreter.\n
    returns : A string containing the path to the script directory.
    """
    from os import path
    import sys
    return path.dirname(sys.executable) if is_executable() else path.dirname(path.realpath(sys.argv[0]))

def local_path(dir_name:str)->str:
    """
    Get the absolute path to a local file/directory, whether running as an executable or in an interpreter.\n
    returns : A string containing the path to the local file/directory
    """
    from os import path
    import sys
    return path.join(sys._MEIPASS, dir_name) if is_executable() else path.join(script_dir(),dir_name)

def pLog(message:str,logFilePath:str='log.txt',max_logs=150):
    """
    Prints and logs the given message to file
    :param message: The message to print/log
    :param logFilePath: The path to the logging file
    """
    import os
    path=os.path.join(script_dir(), logFilePath)
    print(message)
    log(message,path,max_logs)
    
def log(message:str,logFilePath:str='log.txt',max_logs=150):
    """
    Logs the given message to file
    :param message: The message to log
    :param logFilePath: The path to the logging file
    """
    import os
    from datetime import datetime
    path=os.path.join(script_dir(), logFilePath)
    message=message.replace('\n',' ').replace('\r',' ')
    try:
        num_lines = sum(1 for line in open(logFilePath))
        if num_lines>=max_logs:
            lines=open(path, 'r').readlines()
            del lines[0]
            lines.append(datetime.now().strftime('[%m/%d/%Y-%H:%M:%S]: ')+message+'\n')
            with open(path,'w') as file:
                file.writelines(lines)
        else:
            with open(path,'a') as file:
                file.write(datetime.now().strftime('[%m/%d/%Y-%H:%M:%S]: ')+message+'\n')
    except IOError:
        with open(path,'w') as file:
            file.write(datetime.now().strftime('[%m/%d/%Y-%H:%M:%S]: ')+message+'\n')