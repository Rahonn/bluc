from codes.basecode import Command

COMMENT_CHAR = '#'

class Comment(Command):
    
    def __init__(self, line, index):
        super().__init__(line, index)
        
    def run(self):
        return True
    
    def get_data(self):
        return None
    