import time

from codes.basecode import Command
import varmanager

class Time(Command):
    
    text = None
    mode = None
    data = None
    
    def __init__(self, line, index):
        super().__init__(line, index)
        self.text = self.line[5::]
    
        self.finddata()
    
        
    def finddata(self):
        
        spanceSplit = self.text.split(" ")
        
        self.mode = spanceSplit[0]
        
        if str(self.mode).lower() == "get":

            self.data = {
                
                "varname": spanceSplit[1]
            }
        

    def run(self) -> bool:
        
        
        if str(self.mode).lower() == "get":
            
            varmanager.vars[self.data["varname"]] = int(time.time())
            
        
        
        return True
    
    
    def get_data(self):
        
        return {
            
            "text": self.text,
            "mode": self.mode,
            "data": self.data
            
        }
    
