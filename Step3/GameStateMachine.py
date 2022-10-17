import state_info
class GameMachine:
    def __init__(self, game):
        self.game = game
        self.state_dict = {}
        for s in state_info.states:
            key = s['name']
            self.state_dict[key] = state_info.state_class_dict[key]()
        self.game.set_state(self.state_dict)

    def run(self):
        directions = ["east", "west", "south", "north"]
        print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
        userInput = ""
        while userInput != "quit":
            print("label0")
            userInput = input()
            #while userInput not in directions:
            #    print("Options: east/west/south/north")
            print("label1")
            self.game.trigger(userInput)
            print("label2")
            userInput=""
        
        print(" You quit the game")
        return 0


    

 