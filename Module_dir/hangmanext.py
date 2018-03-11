###hangman game redone
##
##class fileaction():
##    def __init__(self,filename):
##        self.filename=filename
##        return none
##    def _loadwords(self): #the _ changes ds to a magic method. magic method is a method
##    #that is only accessible by methods in the same class
##        wordfile=open(self.filename,"r")
##        content=wordfile.read()
##        wordfile=content.split()
##        return wordlist
##    def pickwords(self):
##        word=random.choice(self._loadwords())
####        return word
##
#Hangman Thought Process
##1) research what the problem is
##2) pick a random word from a list
##3)allow the user guess d word by guessing d letters of the word
##4) check to ensure only one (single) alphabeth
##5) check to be sure the input is an alphabeth
##6) you dont want the player to repeat alphabeth
##7)ensure the correct guess is displayed in dia correct position for d given word

import random
class FileAction():
    def _loadwords(filename): #the _ changes ds to a magic method. magic method is a method
                            #that is only accessible by methods in the same class
        wordfile=open(filename,"r")
        content=wordfile.read()
        wordlist=content.split()
        return wordlist

    @classmethod #allows this metod to be called without the instance of the classlk
    def pick_random_words(self,filename):
        wordlist=self._loadwords(filename)
        word=random.choice(wordlist)
        return word
