from Rooms import mainentrance
from .state import State
class MainEntranceState(State):
    def __init__(self):
        self.entity = mainentrance.MainEntrance
        
    def say_hello(self):
        print("You are entering the mainentrance room!")
    
    def say_goodbye(self):
        print("You are leaving the mainentrance room!")
