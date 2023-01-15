from codes.basecode import Command
import varmanager

class PrintVar(Command):
    
    varName = None
    
    def __init__(self, line, index):
        super().__init__(line, index)
        self.varName = self.line[9::]
        
    def run(self) -> bool:
        try:
            
            print(varmanager.vars[self.varName])
            
        except:
            
            return False
            
        return True
    
    def get_data(self):
        
        return {
            
            "varName": self.varName
            
        }
        
        
    
