from numpy import mat

from .place import Place
class ShadowFigure(Place):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __str__(self):
        return "shadow figure"
    def run(self, ):
        anotherinput = True
        print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
        userInput = ""
        while anotherinput:
            userInput = input()
            match userInput:
                case "east":
                    anotherinput=False
                    self.neighbour_map["east"].run()
                case "fight":
                    anotherinput=False
                    print("well done!")