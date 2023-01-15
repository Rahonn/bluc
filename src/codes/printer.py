from codes.basecode import Command

class Printer(Command):
    
    text = None
    
    def __init__(self, line, index):
        super().__init__(line, index)
        self.text = self.line[6::]
        
    def run(self):
        
        print(self.text)
        return True
    
    def get_data(self):
        
        return {
            
            "line": self.line,
            "text": self.text,
            
        }
        
    