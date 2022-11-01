from asyncio.windows_events import NULL
from .room import Room

class HauntedRoom(Room):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __str__(self):
        return "huntedroom"
    def run(self):
        directions = ["south"]
        print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
        userInput=""
        while userInput not in directions:
            print("looks like you can only go back")
            userInput = input()
        self.get_neighbour(userInput).run()
        return NULL

    
