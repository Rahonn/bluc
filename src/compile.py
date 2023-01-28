import pickle

import varmanager

class CompileSave:
    
    cmdList = None
    
    def __init__(self, cmdList):
        
        self.cmdList = cmdList
        
    def load(self):
        
        varmanager.commandsList = self.cmdList
        
    def save(self, cmdList):
        
        self.cmdList = cmdList


def save(compS, filename="build.cbluc"):
    
    with open(filename, "wb") as f:
        
        pickle.dump(compS, f)
    
def load(filename="build.cbluc"):
    
    with open(filename, "rb") as f:
        
        obj = pickle.load(f)
        
    obj.load()
    
