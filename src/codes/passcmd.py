from codes.basecode import Command

class PassCmd(Command):
    
    def __init__(self, line, index):
        super().__init__(line, index)
        
    def run(self) -> bool:
        return True
    
    def get_data(self):
        return None
    
    
