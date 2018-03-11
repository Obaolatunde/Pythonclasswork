from hangmanext.FileAction import pick_random_words as prw

#we can import prw dirctly because its a classmethod and hence doesnot
#require instatiation since it has @classmethod before it

#to access hidden method:fa._FileAction._loadwords

class GameProcess():
##class variables. available to all methods within the class

    word=pick_random_words("words.txt")
    length = len(word)
    max_attempts = length + 1
    available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

    def _getguess():
        guess = input("\n\n  Please guess an alphabet: ".upper()).lower()
        return guess

    def _progress_so_far(word,guessed_letters):
        newstring = []
        for index in range(len(word)):
            letters = word[index]
            if letters in guessed_letters:
                newstring.append(letters)
            else:
                newstring.append("_")
        return newstring

    def _del_alphabeth(alphabeth,choice_range):
        if alphabeth in choice_range:
            letters_remaining = str.replace(choice_range,alphabeth,"_ ")
            return letters_remaining
    @classmethod
    def eval_guess(self):
        guess= self._getguess() #usage includes self cos definition is within the class
        word=self.word
        max_attempts = self.length + 1
        guessed_letters = []
        newstring = []
        correct_guesses = 0
        wrong_guesses = 0
        while True  and max_attempts > 0:
            while (guess == '' or len(guess) > 1) : 
                print ("  Guess must be a single letter !")
                guess =self._getguess()
            if guess in guessed_letters:
                print (" This letter has been guessed!")
                guess =self._getguess()
            
            else:
                guessed_letters.append(guess)
                if guess not in word:
                    print ("   Opps!", guess.upper(), "is not in the word")
                    print ("\t\t\t   -----------------")
                    max_attempts -= 1  
                    print ("  you have ", max_attempts, "attempts left")
                    available_letters =self.del_alphabeth(guess,available_letters)
                    print ("  Available letters: ", available_letters)
                    wrong_guesses += 1
                    guess =self._getguess()

                else:  
                    print ("   Good guess: '", guess, "' appeared", self.word.count(guess), "times")
                    print ("   progress so far: ",self.progress_so_far(self.word,guessed_letters))
                    available_letters = self._del_alphabeth(guess,available_letters)
                    print ("\n  Available Letters:  ", available_letters)

                    correct_guesses += self.word.count(guess)  
                    if  correct_guesses == self.length:
                        print (" \n\n\t\t Great Job! the word is ", self.word.upper(), "!!!")
                        print ("\t\t wrong guesses: ",wrong_guesses)
                        break
                    else:
                        guess =self._getguess()
        else:
            print ("\n\t\t\t\t ************************************")
            print ("\t\t\t\tGame Over! somebody got screwed".upper()) 
            print ("\t\t\t\t ************************************")
            print ("\n\t\t The word is ", self.word.upper())
            exit()
