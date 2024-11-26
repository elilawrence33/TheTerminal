from input.input_handler import InputHandler
from input.game_word import GameWord
from textblob import TextBlob

def start(): 
    game_word = GameWord("hello")

    print(game_word.__synonyms)
    inputHandler = InputHandler()
    inputHandler.collectInput() 

# GAME START
start()