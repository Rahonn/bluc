import sys
import colorama
from colorama import Fore

from codes.basecode import Command
import varmanager

class FnStart(Command):

    commandList = None
    name = None
    text = None

    def __init__(self, line, index):
        super().__init__(line, index)
        self.text = self.line[6::]

        self.name = self.text

        self.commandList = []


    def run(self):

        cindex = varmanager.commandsList.index(self) if self.index is None else self.index

        startingIndex = cindex + 1
        length = len(varmanager.commandsList)

        for i in range(startingIndex, length):

            item = varmanager.commandsList[i]

            if type(item) == FnEnd:

                break

            self.commandList.append(item)


        varmanager.functions[self.name] = self.commandList

        for item in self.commandList:

            varmanager.commandsList.remove(item)

        return True

    def get_data(self):

        return {

            "commandList": self.commandList,
            "name": self.name,
            "text": self.text

        }

class FnEnd(Command):

    def __init__(self, line, index):
        super().__init__(line, index)

    def run(self):

        return True

    def get_data(self):

        return None

class FnCall(Command):

    name = None
    text = None

    def __init__(self, line, index):
        super().__init__(line, index)
        self.text = self.line[7::]
        self.name = self.text

    def run(self):

        cmdList = varmanager.functions[self.name]

        for cc in cmdList:

            cmdr = cc.run()

            if not cmdr:
                print(f"{Fore.RED}\nError!!!{Fore.RESET}\n")
                print(cc.line)
                print(f"\n{Fore.BLUE}^")
                print("| Error on this line\n")
                sys.exit(0)

        return True

    def get_data(self):

        return {

            "name": self.name,
            "text": self.text

        }