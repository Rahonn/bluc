import re

from codes.printer import Printer
from codes.comment import Comment, COMMENT_CHAR
from codes.errorout import ErrorOut
from codes.setvars import SetVars
from codes.printvar import PrintVar
from codes.inputtovar import Input
from codes.mathcmd import MathCmd
from codes.delaycmd import Delay
from codes.ifcmd import IfCmd
from codes.runifcmd import RunIfCmd
from codes.exitcmd import ExitCmd
from codes.importcmd import ImportCmd
from codes.passcmd import PassCmd
from codes.loops import LoopStart, LoopEnd, LoopBreak
from codes.files import ReadFile, WriteFile
from codes.stringcmd import ConcatString


def getCommand(line, index=None):
    
    
    if re.search(r"^PRINT ", line, re.MULTILINE):
        
        return Printer(line, index)
    
    if re.search(f"^{COMMENT_CHAR}", line, re.MULTILINE) or line.strip() == "":
        
        return Comment(line, index)
    
    if re.search(r"^SET ", line, re.MULTILINE):
        
        return SetVars(line, index)
    
    if re.search(r"^PRINTVAR ", line, re.MULTILINE):
        
        return PrintVar(line, index)
    
    if re.search(r"^INPUT ", line, re.MULTILINE):
        
        return Input(line, index)
    
    if re.search(r"^MATH", line, re.MULTILINE):
        
        return MathCmd(line, index)
    
    if re.search(r"^DELAY", line, re.MULTILINE):

        return Delay(line, index)
    
    
    if re.search(r"^IF", line, re.MULTILINE):
        
        return IfCmd(line, index)
    
    if re.search(r"^RUNIF", line, re.MULTILINE):

        return RunIfCmd(line, index)
    
    if re.search(r"^EXIT", line, re.MULTILINE):
        
        return ExitCmd(line, index)
    
    if re.search(r"^IMPORT", line, re.MULTILINE):
        
        return ImportCmd(line, index)
    
    if re.search(r"^PASS", line, re.MULTILINE):
        
        return PassCmd(line, index)

    if re.search(r"^LOOP", line, re.MULTILINE):
        
        return LoopStart(line, index)
    
    
    if re.search(r"^ENDLOOP", line, re.MULTILINE):
        
        return LoopEnd(line, index)
    
    if re.search(r"^BREAKLOOP", line, re.MULTILINE):
        
        return LoopBreak(line, index)
    
    if re.search(r"^READFILE", line, re.MULTILINE):

        return ReadFile(line, index)

    if re.search(r"^CONCAT", line, re.MULTILINE):

        return ConcatString(line, index)
    
    if re.search(r"^WRITEFILE", line, re.MULTILINE):
        
        return WriteFile(line, index)
        
    return ErrorOut(line, index)
        
    
