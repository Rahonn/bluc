import sys
import colorama
from colorama import Fore

import commands
import varmanager
from codes.errorout import ErrorOut



def modeI():
    
    with open(sys.argv[2], "r") as f:

        fileData = f.read()
        
    lines = fileData.split("\n")
    
    for line in lines:
        
        cmd = commands.getCommand(line)
        
        varmanager.commandsList.append(cmd)
        
    for cmd in varmanager.commandsList:
        
        if not cmd.run():

            print(f"{Fore.RED}\nError!!!{Fore.RESET}\n")
            print(lines[varmanager.commandsList.index(cmd)])
            print(f"\n{Fore.BLUE}^")
            print("| Error on this line\n")
            sys.exit(0)
 

def modeD():
    
    print(f"{Fore.BLUE}Running code...{Fore.GREEN}\n")
    modeI()
    print(f"{Fore.CYAN}")
    varmanager.var_dump()
    varmanager.vars = varmanager.defaultvars
    print(f"{Fore.BLUE}")
    isgood = input("Is this ok? (y or n): ")
    if isgood == "y":
        
        print(f"{Fore.BLUE}Thanks for using BLUC")
        
    else:
        
        print(f"{Fore.BLUE}Goodbye!{Fore.RESET}")
        
    
def modeH():
    
    print(f"\t{Fore.CYAN}Code Help{Fore.RESET}")
    print(f"{Fore.BLUE}Print\t-\tTo print something out\t-\tPRINT [string]")
    print("Print Var\t-\tTo print a var out\t-\tPRINTVAR [varname]")
    print("Set\t-\tTo set a var\t-\tSET [varname] = [value]")
    print("Input\t-\tTo get user input\t-\tINPUT [varname]")
    print("Math\t-\tOperators +, -, *, /, **, RAND and store the result to a new var. If you are using RAND you can make num1 and num2 @ for no set range\t-\tMATH [varname] [operator] [num1] [num2]")
    print("Delay\t-\tAdd a delay to your code. You can use a var just place a varname in it but put a $ at the start\t-\tDELAY [seconds]")
    print("Comments\t-\tUse # for comments\t-\t# [comment]")
    print("If\t-\tAn if system. Replace varname with the name of the outvar, replace args with the args use for string with this put a ! at the start and end and if you are using a var as a arg put a $ at the start of it's name\t-\tIF [varname] [arg1] [op] [arg2] :[outiftrue]:[outiffalse]:")
    print(
        "Run If\t-\tAn if system. Replace args with the args use for string with this put a ! at the start and end and if you are using a var as a arg put a $ at the start of it's name, replace [outcmdiftrue] with the command to run if the if is true same for the [outcmdiffalse] but for false instead\t-\tRUNIF [arg1] [op] [arg2] |[outcmdiftrue]|[outcmdiffalse]|")
    print("Exit\t-\tExit the app\t-\tEXIT")
    print("Import\t-\tUse the import command to load code from a different file. Replace [path] with the path to the bluc file include the file extension\t-\tIMPORT [path]")
    print("Pass\t-\tThis command does not do anything!\t-\tPASS")
    print(
        "Loops\t-\tUse LOOPSTART [index varname] [times] replace [times] with @ for a infinite number of times. Use BREAKLOOP to break out of a loop. Use ENDLOOP to end a loop\t-\t\n\tLOOP index 5\n\tPRINTVAR index\n\tRUNIF $index == 3 |BREAKLOOP|PASS|\n\tENDLOOP")
    print()
    print(f"\t{Fore.RED}Comands Options{Fore.RESET}")
    print(f"{Fore.MAGENTA}Interpret\t-\tTo run code\t-\t./BLUC -i [filename]")
    print("Debug\t-\tInterprets and Compiles your code\t-\t./BLUC -d [filename]")
    print("Help\t-\tTo get this info\t-\t./BLUC --help")
    print(f"Version\t-\tTo get the BLUC version number\t-\t./BLUC --version{Fore.RESET}")
    modeV()

def modeV():
    
    print(f'{Fore.LIGHTGREEN_EX}BLUC version: {varmanager.vars["VERSION"]}{Fore.RESET}')     

if len(sys.argv) <= 1:
    
    print(f'{Fore.LIGHTGREEN_EX}Welcome to BLUC (Better Language universal code)!{Fore.RESET}')
    modeH()
    sys.exit(0)

mode = sys.argv[1]
            
if mode.lower() == "-i":
    
    modeI()

if mode.lower() == "-d":
    
    modeD()

if mode.lower() == "--help" or mode.lower() == "-help" or mode.lower() == "-h":
    
    modeH()
    
if mode.lower() == "--version" or mode.lower() == "-version" or mode.lower() == "-v":

    modeV()
    
