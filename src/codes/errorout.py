from codes.basecode import Command

class ErrorOut(Command):
    
    def __init__(self, line, index):
        super().__init__(line, index)
        
    def run(self) -> bool:
        return False
    
    def get_data(self):
        return None
    
