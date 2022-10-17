class Map():
    def __init__(self):
        self.location_map = {}
    def add_entity(self, id, entity):
        self.location_map[id] = entity