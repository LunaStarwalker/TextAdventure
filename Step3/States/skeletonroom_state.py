from Places import skeletonroom
from .state import State
class SkeletonRoomState(State):
    def __init__(self):
        self.entity = skeletonroom.SkeletonRoom()
    
    def say_hello(self):
        print("You are entering the skeleton room!")
    
    def say_goodbye(self):
        print("You are leaving the skeleton room!")
    
