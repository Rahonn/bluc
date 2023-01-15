import re

from codes.basecode import Command
import varmanager

class ConcatString(Command):

    arg1 = None
    arg2 = None
    varname = None
    text = None
    arg1IsStr = None
    arg2IsStr = None
    arg1IsVar = None
    arg2IsVar = None

    def __init__(self, line, index):

        super().__init__(line, index)

        self.text = self.line[7::]

        spaceSpilt = self.text.split(" ")

        conSplit = self.text.split("|")

        self.varname = spaceSpilt[0]
        self.arg1 = str(conSplit[1])
        self.arg2 = str(conSplit[2])


        self.varTest()

        

    
    def varTest(self):

        if not re.search(r"^\$", str(self.arg1)):
            
            self.arg1IsStr = True
            self.arg1IsVar = False

        else:

            self.arg1IsStr = False
            self.arg1IsVar = True


        if not re.search(r"^\$", str(self.arg2)):

            self.arg2IsStr = True
            self.arg2IsVar = False

        else:

            self.arg2IsStr = False
            self.arg2IsVar = True

    def varTestFinal(self):

        
        if self.arg1IsVar:

            self.arg1 = str(varmanager.vars[self.arg1[1::]])

        else:

            self.arg1 = str(self.arg1)

        
        if self.arg2IsVar:
            self.arg2 = str(varmanager.vars[self.arg2[1::]])

        else:

            self.arg2 = str(self.arg2)

    def run(self):

        try:

            self.varTestFinal()
            self.varTest()
            self.varTestFinal()

        except:

            return False
        
        
        self.arg1 = self.arg1.replace("\\n", "\n")
        self.arg2 = self.arg2.replace("\\n", "\n")

        
        varmanager.vars[self.varname] = f"{str(self.arg1)}{str(self.arg2)}"


        return True

    def get_data(self):

        return {

            "arg1": self.arg1,
            "arg2": self.arg2,
            "arg1IsStr": self.arg1IsStr,
            "arg2IsStr": self.arg2IsStr,
            "arg1IsVar": self.arg1IsVar,
            "arg2IsVar": self.arg2IsVar,
            "text": self.text,
            "varname": self.varname

        }
        
