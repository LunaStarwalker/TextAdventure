
from transitions import Machine
import GameStateMachine
import game
import state_info
class MyAdventureGame():
    
    def __init__(self):
        # Initialize
        self.game = game.Game()
        self.machine = Machine(self.game, 
                               states= state_info.states, 
                               transitions=state_info.transitions, 
                               initial='mainentrance')
        self.game_state_machine = GameStateMachine.GameMachine(self.game)

    def run(self):
        print("Welcome to the Adventure Game!")
        print("As an avid traveller, you have decided to visit the Catacombs of Paris.")
        print("However, during your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, " +name+ ".")
        self.game_state_machine.run()
        

if __name__ == "__main__":
    mygame = MyAdventureGame()
    mygame.run()