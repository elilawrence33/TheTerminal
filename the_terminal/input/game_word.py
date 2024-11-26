from textblob import Word

class GameWord: 

    def __init__(self, word): 
        __word_string = word
        __word = Word(word)
        self.__create_synonyms(__word)

    @property
    def __word_string(self): 
        return self.__word_string
    
    @property
    def __word(self): 
        return self.__word
    
    @property
    def __synonyms(self): 
        return self.__synonyms
    
    @__word_string.setter
    def __word_string(self, value): 
        if not value:
            raise ValueError("Word string cannot be blank")
        self.__word_string = value

    @__synonyms.setter
    def __synonyms(self, value): 
        if not value: 
            raise ValueError("Synonyms cannot be blank")
        self.__synonyms = value

    
    # Class Methods

    def __create_synonyms(self, word):
        synonym_list = word.synsets
        lemmatized_syn_set = set()  # Use a set to store unique synonyms
        for synonym in synonym_list: 
            lemmatized_syn_set.update(synonym.lemma_names())  # Add all lemma names to the set

        self.__synonyms = list(lemmatized_syn_set) 
    


