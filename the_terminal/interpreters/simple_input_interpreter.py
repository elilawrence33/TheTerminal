from abc_input_interpreter import ABCInputInterpreter

'''
    This class defines a simple input interpreter which does not use machine learning. 
'''
class SimpleInputInterpreter(ABCInputInterpreter): 
    
    def interpret(self, input):
        self.__determineCommand(input)

    def __determineCommand(self, input): 
        print()