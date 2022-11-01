from asyncio.windows_events import NULL
from .room import Room

class MainEntrance(Room):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __str__(self):
        return "mainentrance"
    def run(self, ):
        directions = ["north","east", "west"]
        print("You are at a crossroads, there is no way going back. Where would you like to go?")
        userInput = ""
        while userInput not in directions:
            print("Options: north/east/west")
            userInput = input()
        self.neighbour_map[userInput].run()
        return True
    
    
