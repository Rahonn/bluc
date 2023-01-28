import sys
import colorama
from colorama import Fore

import commands
import varmanager
from codes.errorout import ErrorOut
import compile



def modeI(filename):
    
    with open(filename, "r") as f:

        fileData = f.read()
        
    lines = fileData.split("\n")
    
    for line in lines:
        
        cmd = commands.getCommand(line)
        
        varmanager.commandsList.append(cmd)
        
    for cmd in varmanager.commandsList:
        
        if not cmd.run():

            print(f"{Fore.RED}\nError!!!{Fore.RESET}\n")
            print(cmd.line)
            print(f"\n{Fore.BLUE}^")
            print("| Error on this line\n")
            sys.exit(0)
 
 
def modeC(filename, out="build.cbluc"):

    with open(filename, "r") as f:

        fileData = f.read()

    lines = fileData.split("\n")

    for line in lines:

        cmd = commands.getCommand(line)

        varmanager.commandsList.append(cmd)

    compile.save(compile.CompileSave(varmanager.commandsList), out)
    
    print(f"{Fore.BLUE}Code Compiled!{Fore.RESET}")
    
def modeRC(filename):

    compile.load(filename)
    
    for cmd in varmanager.commandsList:

        if not cmd.run():

            print(f"{Fore.RED}\nError!!!{Fore.RESET}\n")
            sys.exit(0)


def modeDRC(filename):

    print(f"{Fore.BLUE}Running code...{Fore.GREEN}\n")
    modeRC(filename)
    print(f"{Fore.CYAN}")
    varmanager.var_dump()
    varmanager.vars = varmanager.defaultvars
    print(f"{Fore.BLUE}")
    isgood = input("Is this ok? (y or n): ")
    if isgood == "y":

        print(f"{Fore.BLUE}Thanks for using BLUC")

    else:

        print(f"{Fore.BLUE}Goodbye!{Fore.RESET}")

def modeD():
    
    print(f"{Fore.BLUE}Running code...{Fore.GREEN}\n")
    modeI(sys.argv[2])
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
    print("Read file\t-\tUse to read files\t-\tREADFILE [outputvar] [filepath]")
    print("Write file\t-\tUse to write files\t-\tWRITEFILE [inputvar] [filepath]")
    print("String Concat\t-\tUse to add 2 vars to together as text. If you add 2 and 3 you will get 23. If your add Hello and World you will get Hello World. Replace [arg1] or [arg2] with plain text or for a var put a $ at the start of the name\t-\tCONCAT [outputvarname] |[arg1]|[arg2]|")
    print("Time Get\t-\tGet the current system time and store the result in a var\t-\tTIME GET [outputvar]")
    print(
        "Functions\t-\tUse FNDEF [functionname]. Use FNEND to end a function. Use FNCALL [functionname] to call a function!\t-\t\n\tFNDEF myFunc\n\tPRINT This is my func\n\tFNEND\n\tFNCALL myFunc\n\tFNCALL myFunc")
    print(
        "Interp\t-\tUse to test if the code is running with a certain interpreter\t-\tINTERP [interpretername]")
    print()
    print(f"\t{Fore.RED}Comands Options{Fore.RESET}")
    print(f"{Fore.MAGENTA}Interpret\t-\tTo run code\t-\t./BLUC -i [filename]")
    print("Debug\t-\tInterprets and Compiles your code\t-\t./BLUC -d [filename]")
    print("Help\t-\tTo get this info\t-\t./BLUC --help")
    print("Run\t-\tUse to run your code\t-\t./BLUC [filename]")
    print("Compile\t-\tUse to compile your code\t-\t./BLUC -c [filename] [outputfile]")
    print(
        "Run Compiled Code\t-\tUse to run your compiled code\t-\t./BLUC -rc [filename] [outputfile]")
    print(
        "Debug Compiled Code\t-\tUse to debug your compiled code\t-\t./BLUC -drc [filename] [outputfile]")
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
    
    modeI(sys.argv[2])

elif mode.lower() == "-d":
    
    modeD()

elif mode.lower() == "-c":
    
    if len(sys.argv) >= 4:
        
        modeC(sys.argv[2], sys.argv[3])
    
    else:
        
        modeC(sys.argv[2])
        
elif mode.lower() == "-rc":
    
    modeRC(sys.argv[2])    
    
elif mode.lower() == "-drc":
    
    modeDRC(sys.argv[2])    

elif mode.lower() == "--help" or mode.lower() == "-help" or mode.lower() == "-h":
    
    modeH()
    
elif mode.lower() == "--version" or mode.lower() == "-version" or mode.lower() == "-v":

    modeV()
    
else:
    
    modeI(sys.argv[1])
