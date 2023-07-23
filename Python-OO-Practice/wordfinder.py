"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Finding random words from text dictionary"""

    def __init__(self,path):
        """Reads dictionary and reports # of items read"""

        dict_file = open(path)

        self.words=self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse (self, dict_file):
        """Parse the dict file into a list of words"""

        return[w.strip() for w in dict_file]
    
    def random(self):
        """Return random word"""

        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Word finder that excludes blank lines/text"""

    def parse(self,dict_file):
        """Parse dict_file into a list of words skipping blank lines/text"""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith('#')]
    
