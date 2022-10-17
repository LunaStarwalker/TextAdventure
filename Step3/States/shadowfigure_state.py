from Rooms import shadowfigure
from .state import State
class ShadowFigureState(State):
    def __init__(self):
        self.entity = shadowfigure.ShadowFigure()
    
    
    def say_hello(self):
        print("You are entering the shadow figure !")
    
    def say_goodbye(self):
        print("You are leaving the shadow figure !")
