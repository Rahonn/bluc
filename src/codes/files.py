from codes.basecode import Command
import varmanager

class ReadFile(Command):

    varname = None
    path = None
    text = None

    def __init__(self, line, index):
        super().__init__(line, index)

        self.text = self.line[9::]

        spaceSpilt = self.text.split(" ")

        self.varname = spaceSpilt[0]
        self.path = spaceSpilt[1]



    def run(self):

        try:

            with open(self.path, "r") as f:

                varmanager.vars[self.varname] = f.read()

        except:

            return False


        return True


    def get_data(self):

        return {

            "varname": self.varname,
            "path": self.path,
            "text": self.text

        }

