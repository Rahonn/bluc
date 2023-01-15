import copy

from codes.basecode import Command
import varmanager


class LoopStart(Command):
    
    commandList = None
    endCmd = None
    index = None
    times = None
    indexVarname = None
    isWhile = None
    
    def __init__(self, line):
        super().__init__(line)
        self.text = self.line[5::]
        
        self.commandList = []
    
    def findData(self):
        
        self.index = varmanager.commandsList.index(self)
        self.indexVarname = self.text.split(" ")[0]
        self.times = self.text.split(" ")[1]
        self.isWhile = False
        
            
            
        if self.times == "@":
            
            self.isWhile = True
            
        else:
            
            self.isWhile = False
            
            try:

                self.times = int(self.times)

            except:

                self.times = varmanager.vars[self.times]



        startingIndex = self.index + 1
        length = len(varmanager.commandsList)
        
        
        for i in range(startingIndex, length):
            
            item = varmanager.commandsList[i]
            
            if type(item) == LoopEnd:
                
                break
            
            self.commandList.append(item)
        
        
    def execute(self):
        
        if self.times == "@":
            
            self.isWhile = True
        
        if self.isWhile:
            

            varmanager.runningLoop = True

            i = 0.0
            
            while True:

                varmanager.vars[self.indexVarname] = float(i)

                if not varmanager.runningLoop:

                    break

                for cmd in self.commandList:

                    ncmd = copy.deepcopy(cmd)

                    if not varmanager.runningLoop:

                        break

                    ncmdg = ncmd.run()

                    if not ncmdg:

                        return False
                    
                i += 1.0

            varmanager.runningLoop = False

            for item in self.commandList:

                varmanager.commandsList.remove(item)
        
        else:
            
            varmanager.runningLoop = True

            for i in range(int(self.times)):

                varmanager.vars[self.indexVarname] = float(i)

                if not varmanager.runningLoop:

                    break

                for cmd in self.commandList:

                    ncmd = copy.deepcopy(cmd)

                    if not varmanager.runningLoop:

                        break

                    
                    ncmdg = ncmd.run()

                    if not ncmdg:

                        return False

            varmanager.runningLoop = False

            for item in self.commandList:

                varmanager.commandsList.remove(item)
    
        
        
    def run(self) -> bool:
        isgood = True
        isgood = self.findData()
        isgood = self.execute()
        return True
    
    
    def get_data(self):
        return {
            
            "commandList": self.commandList,
            "endCmd": self.endCmd,
            "index": self.index,
            "times": self.times
            
        }
    
    

class LoopEnd(Command):
    
    def __init__(self, line):
        super().__init__(line)
        
        
    def run(self) -> bool:
        return True
    
    
    def get_data(self):
        return None
    

class LoopBreak(Command):
    
    def __init__(self, line):
        super().__init__(line)

    def run(self) -> bool:
        varmanager.runningLoop = False
        return True
    
    def get_data(self):
        return None
    
    

