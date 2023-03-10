import re
import time

from codes.basecode import Command
import varmanager

class Delay(Command):
    
    time = None
    
    def __init__(self, line, index):
        super().__init__(line, index)
        self.time = line[6::]
    
    def run(self) -> bool:
        
        if re.search(r"^\$", self.time):
            
            self.time = float(varmanager.vars[self.time[1::]])
            
        
        try:
            
            time.sleep(float(self.time))
            
        except:
            
            return False
        
        return True
    

    def get_data(self):
        
        return {
            
            "time": self.time
            
        }
