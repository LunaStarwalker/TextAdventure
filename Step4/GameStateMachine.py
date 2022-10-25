import state_info
class GameMachine:
    def __init__(self):
        self.state_dict = {}
        self.key = ""
        for s in state_info.states:
            key = s['name']
            self.state_dict[key] = state_info.state_class_dict[key]()
        
    def set_state(self, state_dict):
        self.state_dict = state_dict

    def say_goodbye(self):
        current_state = self.state_dict[self.state]
        current_state.say_goodbye()
        
    def say_hello(self):
        current_state = self.state_dict[self.state]
        self.key = current_state.say_hello()
        
    def run(self):
        self.say_hello()
        while self.key !='quit':    
            if self.key in ["east", "west", "south", "north"]:
                self.trigger(self.key)
            else:
                print("key is not valid")
                break
    
        print("You quit the game!")
       


    

 