from .room import Room

class MainEntrance(Room):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __str__(self):
        return "mainentrance"
    def run(self, ):
        directions = ["left","right","forward"]
        print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
        userInput = ""
        while userInput not in directions:
            print("Options: left/right/backward/forward")
            userInput = input()
            if userInput == "left":
                showShadowFigure()
            elif userInput == "right":
                showSkeletons()
            elif userInput == "forward":
                hauntedRoom()
            elif userInput == "backward":
                print("You find that this door opens into a wall.")
            else: 
                print("Please enter a valid option.")
    
    