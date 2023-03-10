import re

from codes.basecode import Command
import varmanager

class IfCmd(Command):
    
    varname = None
    arg1 = None
    arg2 = None
    op = None
    iftrue = None
    iffalse = None
    text = None
    arg1isNum = None
    arg2isNum = None
    arg1isVar = None
    arg2isVar = None
    arg1isStr = None
    arg2isStr = None
    
    def __init__(self, line, index):
        super().__init__(line, index)
        self.text = line[3::]
        
        spaceSpilt = self.text.split(" ")
        
        self.varname = spaceSpilt[0]
        self.arg1 = spaceSpilt[1]
        self.op = spaceSpilt[2]
        self.arg2 = spaceSpilt[3]
        
        conSplit = self.text.split(":")
        
        self.iftrue = conSplit[1]
        self.iffalse = conSplit[2]
        
        self.iftest()
        
        
        
    def iftest(self):
        
        try:

            float(self.arg1)
            self.arg1isNum = True
            self.arg1isVar = False

        except:

            self.arg1isNum = False

        try:

            float(self.arg2)
            self.arg2isNum = True
            self.arg2isVar = False

        except:

            self.arg2isNum = False

        if re.search(r"^\$", str(self.arg1)):

            self.arg1isVar = True

        else:

            self.arg1isVar = False

        if re.search(r"^\$", str(self.arg2)):

            self.arg2isVar = True

        else:

            self.arg2isVar = False

        if re.search(r"^!.+$", str(self.arg1)):

            self.arg1isStr = True

        else:

            self.arg1isStr = False

        if re.search(r"^!.+$", str(self.arg2)):

            self.ar21isStr = True

        else:

            self.arg2isStr = False

        if re.search(r"^[!]", str(self.arg1)) and re.search(r"[!]$", str(self.arg1)):

            self.arg1isStr = True

        else:

            self.arg1isStr = False

        if re.search(r"^[!]", str(self.arg2)) and re.search(r"[!]$", str(self.arg2)):

            self.arg2isStr = True

        else:

            self.arg2isStr = False

        if self.arg1isNum:

            self.arg1isNum = True
            self.arg1isVar = False
            self.arg1isStr = False

        if self.arg1isVar:

            self.arg1isNum = False
            self.arg1isVar = True
            self.arg1isStr = False

        if self.arg1isStr:

            self.arg1isNum = False
            self.arg1isVar = False
            self.arg1isStr = True

        if self.arg2isNum:

            self.arg2isNum = True
            self.arg2isVar = False
            self.arg2isStr = False

        if self.arg2isVar:

            self.arg2isNum = False
            self.arg2isVar = True
            self.arg2isStr = False

        if self.arg2isStr:

            self.arg2isNum = False
            self.arg2isVar = False
            self.arg2isStr = True


    
    
    def iftestfinal(self):
        
        if self.arg1isVar:

            self.arg1 = varmanager.vars[self.arg1[1::]]

        if self.arg1isStr:

            self.arg1 = str(self.arg1[1:][:-1])

        if self.arg2isNum:

            self.arg2 = float(self.arg2)

        if self.arg2isVar:

            self.arg2 = varmanager.vars[self.arg2[1::]]

        if self.arg2isStr:

            self.arg2 = str(self.arg2[1:][:-1])
            
        if self.arg1isNum:

            self.arg1 = float(self.arg1)
        
            
            

        
    def run(self) -> bool:
        
        try:
            
            self.iftestfinal()
            self.iftest()
            self.iftestfinal()
            
        except:
            
            return False
            
        
        
        didIf = False

        try:
            
            if self.op == "<":

                if self.arg1 < self.arg2:
                    
                    varmanager.vars[self.varname] = self.iftrue
                    didIf = True
                    
                else:
                    
                    varmanager.vars[self.varname] = self.iffalse
                    didIf = True
                    
            if self.op == ">":

                if self.arg1 > self.arg2:

                    varmanager.vars[self.varname] = self.iftrue
                    didIf = True

                else:

                    varmanager.vars[self.varname] = self.iffalse
                    didIf = True
                    
            if self.op == "==":

                if self.arg1 == self.arg2:

                    varmanager.vars[self.varname] = self.iftrue
                    didIf = True

                else:

                    varmanager.vars[self.varname] = self.iffalse
                    didIf = True
            
            if self.op == "!=":

                if not self.arg1 == self.arg2:

                    varmanager.vars[self.varname] = self.iftrue
                    didIf = True

                else:

                    varmanager.vars[self.varname] = self.iffalse
                    didIf = True
                    
            if self.op == ">=":

                if self.arg1 >= self.arg2:

                    varmanager.vars[self.varname] = self.iftrue
                    didIf = True

                else:

                    varmanager.vars[self.varname] = self.iffalse
                    didIf = True
                    
            if self.op == "<=":

                if self.arg1 <= self.arg2:

                    varmanager.vars[self.varname] = self.iftrue
                    didIf = True

                else:

                    varmanager.vars[self.varname] = self.iffalse
                    didIf = True
                    
        except:
            
            return False
            

        return didIf
    
    
    def get_data(self):
        return {
            
            "varname": self.varname,
            "arg1": self.arg1,
            "arg2": self.arg2,
            "op": self.op,
            "iftrue": self.iftrue,
            "iffalse": self.iffalse,
            "text": self.text,
            "arg1isNum": self.arg1isNum,
            "arg2isNum": self.arg2isNum,
            "arg1isVar": self.arg1isVar,
            "arg2isVar": self.arg2isVar,
            "arg1isStr": self.arg1isStr,
            "arg2isStr": self.arg2isStr
            
        }
    
