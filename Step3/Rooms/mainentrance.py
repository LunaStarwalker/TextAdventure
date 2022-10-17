from .room import Room

class MainEntrance(Room):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __str__(self):
        return "maintrance"
    
    