import sys
import colorama
from colorama import Fore

from codes.basecode import Command

class Interp(Command):
    
    using = None
    text = None
    
    def __init__(self, line, index):
        super().__init__(line, index)
        self.text = self.line[7::]
        
        self.using = self.text
        
    def run(self):
        
        if not self.using.lower() == "bluc":
            
            print(f"{Fore.RED}NOTE: The code was made for {self.using} but this is BLUC!{Fore.RESET}")
            dorun = input(f"{Fore.BLUE}Do you want to run this code anyway? (y or n): ")
            print(f"{Fore.RESET}", end="")
            
            if dorun.lower() == "y":
                
                return True
            
            else:
                
                sys.exit(0)
        
        return True
    
    def get_data(self):
        return {
            
            "using": self.using,
            "text": self.text
            
        }
