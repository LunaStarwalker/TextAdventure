from Places import skeletonroom
from .state import State
class SkeletonRoomState(State):
    def __init__(self):
        self.entity = skeletonroom.SkeletonRoom()
    
    def say_hello(self):
        print("You are entering the skeleton room!")
        directions = ["east", "west", "south", "north"]
        userInput = ""
        while userInput != "quit":
            if userInput in directions:
                return userInput
            else:
                available_command = ["look to left", "look to right", "north", "south"]
                if userInput in available_command:
                  match userInput:
                    case "look to left": 
                        print("You find that this door opens into a wall. ")
                        print("You open some of the drywall to discover a knife.")
                        self.weapon = True
                    case "look to right":
                        print("You see a wall of skeletons as you walk into the room.") 
                        print("Someone is watching you. Where would you like to go?")
                else:
                  print("available command: ", available_command)  

            userInput = input()  
        return "quit"
    
    def say_goodbye(self):
        print("You are leaving the skeleton room!")
    
