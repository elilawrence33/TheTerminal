from abc_input_interpreter import ABCInputInterpreter

class InputInterpreter(ABCInputInterpreter): 

    def interpret(self, input):
        self.determineCommand(input)

    def determineCommand(self, input): 
        