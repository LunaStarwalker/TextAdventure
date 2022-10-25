from Rooms import hauntedroom, mainentrance, skeletonroom
from Places import shadowfigure

class MyAdventureGame():
    def __init__(self):
        self.hauntedroom = hauntedroom.HauntedRoom()
        self.mainentrance = mainentrance.MainEntrance()
        self.skeletonroom = skeletonroom.SkeletonRoom()
        self.shadowfigure = shadowfigure.ShadowFigure()
    def run(self):
        while True:
            print("Welcome to the Adventure Game!")
            print("As an avid traveller, you have decided to visit the Catacombs of Paris.")
            print("However, during your exploration, you find yourself lost.")
            print("You can choose to walk in multiple directions to find a way out.")
            print("Let's start with your name: ")
            name = input()
            print("Good luck, " +name+ ".")
            self
            
            
          

if __name__ == "__main__":
    mygame = MyAdventureGame()
    mygame.run()
    