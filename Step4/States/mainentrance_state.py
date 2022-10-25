from weakref import WeakSet
from Rooms import mainentrance
from .state import State
class MainEntranceState(State):
    def __init__(self):
        self.entity = mainentrance.MainEntrance
        
    def say_hello(self):
        print("You are entering the mainentrance!")
        directions = ["east", "west", "south", "north"]
        print("You are at a crossroads, ")
        print("and you can choose to go down any of the four hallways. ")
        print("Where would you like to go?")
    
        userInput = ""
        while userInput != "quit":
            if userInput in directions:
                return userInput
            else:
             match userInput:
                case "look to left": 
                    print("You find that this door opens into a wall. ")
                    print("You open some of the drywall to discover a knife.")
                    self.weapon = True
                case "look to right":
                    print("You see a wall of skeletons as you walk into the room.") 
                    print("Someone is watching you. Where would you like to go?")

            print("available command: ", directions)  
            userInput = input()  
        return "quit"
    def say_goodbye(self):
        print("You are leaving the mainentrance !")
