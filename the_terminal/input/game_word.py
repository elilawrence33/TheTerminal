from textblob import Word
import nltk

class GameWord: 
    WORDNET = "wordnet"

    def __init__(self, word, synonyms=None):
        nltk.download(self.WORDNET)
        __word = Word(word)
        self.__create_synonyms(__word)
    
    @property
    def word(self): 
        return self.__word
    
    @word.setter
    def word(self, value):
        if not value:
            raise ValueError("Word cannot be blank")
        self.__word = value

    @property
    def synonyms(self): 
        return self.__synonyms
    
    @synonyms.setter
    def synonyms(self, value): 
        if not value: 
            raise ValueError("Synonyms cannot be blank")
        self.__synonyms = value

    # Class Methods

    def __create_synonyms(self, word):
        synonym_list = word.synsets
        lemmatized_syn_set = set()  # Use a set to store unique synonyms
        print(synonym_list)
        # for synonym in synonym_list: 
        #     lemmatized_syn_set.update(synonym.lemma_names())  # Add all lemma names to the set

        # self.__synonyms = list(lemmatized_syn_set) 
