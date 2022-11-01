from Rooms import hauntedroom, mainentrance, skeletonroom
from Places import shadowfigure


class MyAdventureGame():

    def __create_location_map(self):
        self.mainentrance.add_neighbour('north', self.hauntedroom)
        self.mainentrance.add_neighbour('west', self.shadowfigure)
        self.mainentrance.add_neighbour('east', self.skeletonroom)
        self.hauntedroom.add_neighbour('south', self.mainentrance)
        self.shadowfigure.add_neighbour('east', self.mainentrance)
        self.skeletonroom.add_neighbour('west', self.mainentrance)
    
    def __init__(self):
        self.hauntedroom = hauntedroom.HauntedRoom()
        self.mainentrance = mainentrance.MainEntrance()
        self.skeletonroom = skeletonroom.SkeletonRoom()
        self.shadowfigure = shadowfigure.ShadowFigure()
        self.__create_location_map()

    def run(self):
        isFinished = False
        while not isFinished:
            print("Welcome to the Adventure Game!")
            print("As an avid traveller, you have decided to visit the Catacombs of Paris.")
            print("However, during your exploration, you find yourself lost.")
            print("You can choose to walk in multiple directions to find a way out.")
            print("Let's start with your name: ")
            name = input()
            print("Good luck, " +name+ ".")
            isFinished = self.mainentrance.run()
            
if __name__ == "__main__":
    mygame = MyAdventureGame()
    mygame.run()
    
