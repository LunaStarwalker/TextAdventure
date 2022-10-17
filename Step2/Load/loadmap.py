from Rooms import mainentrance, hauntedroom, skeletonroom
from Places import shadowfigure
import numpy as np
from .map import Map
import os
map_width = 3
map_height = 2
map_file = "map.txt"

place_class_dict = {"mainentrance": mainentrance.MainEntrance, 
                    "hauntedroom": hauntedroom.HauntedRoom,
                    "shadowfigure": shadowfigure.ShadowFigure,
                    "skeletonroom": skeletonroom.SkeletonRoom}

class LoadMap:
    def __init__(self):
        self.game_map = Map()
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        self.entity_list = open(os.path.join(__location__, map_file)).read().split()
        print(self.entity_list)
        self.build_map()
        self.print_map()
    
    def print_map(self):
        for key in self.game_map.location_map:
            entity = self.game_map.location_map[key]
            print( entity, "west neighbour: ", entity.west)
            print("esat neighbour: ", entity.east)
            print("south neighbour: ", entity.south)
            print("north neighbour: ", entity.north)


    def map_func(self, classid):
        if classid != "##":
            return place_class_dict[classid]()
        else:
            return None  

    def add_neighbour(self, i,j, entity):
        if(i>0 ):
            neighbour = self.game_class_array[i-1][j]
            entity.west = neighbour if neighbour!=None else None
        if(j>0): 
            neighbour = self.game_class_array[i][j-1]
            entity.north = neighbour if neighbour!=None else None         
        if(i<(map_height-1)): 
            neighbour = self.game_class_array[i+1][j]
            entity.south = neighbour if neighbour!=None else None           
        if(j<(map_width-1)):
            neighbour = self.game_class_array[i][j+1]
            entity.east = neighbour if neighbour!=None else None
                    
    def build_map(self):
        self.game_class_array = np.array(list(map(self.map_func, self.entity_list)))\
                                  .reshape((map_height, map_width))

        for (i,j), entity in np.ndenumerate(self.game_class_array):
            if(entity):
                self.game_map.add_entity(entity.__str__, entity)
                self.add_neighbour( i,j, entity)