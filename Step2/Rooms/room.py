class Wall:
    def __init__(self, color, description):
        self.color = color
        self.description= description

class Door:
    pass

class Window:
    pass

class Room:
    def __init__(self, **kwargs):
        self.neighbour_map={}
        
    def buide_room(self):
        pass

    def add_neighbour(self, direction, neighbour):
        self.neighbour_map[direction] = neighbour
        
    def get_neighbour(self, direction):
        return self.neighbour_map[direction]