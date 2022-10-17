
class Game():
    
    def set_state(self, state_dict):
        self.state_dict = state_dict


    def say_goodbye(self):
        current_state = self.state_dict[self.state]
        current_state.say_goodbye()
        print(self.state)
    def say_hello(self):
        current_state = self.state_dict[self.state]
        current_state.say_hello()
        print(self.state)