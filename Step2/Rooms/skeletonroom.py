from .room import Room

class SkeletonRoom(Room):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon = False
    def __str__(self):
        return "SkeletonRoom"
    def run(self):
        anotherinput = True
        print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
        userInput = ""
        while anotherinput:
            userInput = input()
            match userInput:
                case "west": 
                    self.neighbour_map["west"].run()
                    anotherinput=False
                case "look around": 
                    self.weapon = True
                    print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
                case _:
                    print("nothing happened. try again")
