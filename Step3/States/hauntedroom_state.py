from Rooms import hauntedroom
from .state import State
class HauntedRoomState(State):
    def __init__(self):
        self.entity = hauntedroom.HauntedRoom
    
    def say_hello(self):
        print("You are entering the haunted room!")
    
    def say_goodbye(self):
        print("You are leaving the skeleton room!")

    