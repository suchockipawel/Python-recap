import random 
from abc import abstractmethod,ABC


class Game(ABC):
    
    @abstractmethod
    def play():
        pass
    
    @abstractmethod
    def check_correct_answer():
        pass
    
class Hangman(Game):
    def __init__(self,name) :
        self._name = name
        self.__world_list =  [
            "python",
            "hangman",
            "game",
            "programming",
            "challenge",
            "polymorphism",
            "abstraction",
        ]
        self._attempts = 3
        self._word = random.choice(self.__world_list)
        self._guessed_letters = set()
        self._check = False
        
    def play(self):
        print(f"Welcome to {self._name}!")
        while self._attempts > 0 and set(self._word) != self._guessed_letters:
            self.display_word()
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in self._guessed_letters:
                    print("you have already guessed the letter")
                elif guess in self._word:
                    self._guessed_letters.add(guess)
                    print("Good guess !")
                else :
                    self._attempts = self._attempts - 1
                    #self._attempts -= 1
                    print(f"Incorrect guess. {self._attempts} attempts left.")
                    
            else:
                print("Invalid input. Please guess a single letter.")
        self.display_result()
                    
            
    def display_word(self):
        display = ''
        for letter in self._word:
            if letter in self._guessed_letters:
                display += letter
            else : 
                display += '_'
        print(display)
        
    def display_result(self):
        if set(self._word) == self._guessed_letters:
            self._check = True
            print(f"Congratulations! You've guessed the word: {self._word}")
        else:
            print(f"Game over! The word was: {self._word}")
            
    def check_correct_answer(self):
        return self._check
        
        

class MathGame(Game):
    def __init__(self,name):
        self._name = name
        self._check = False
    def play(self):
        print(f"Welcome to {self._name}!")
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        result = num1 + num2
        user_input = int(input(f"What is {num1} + {num2}? "))
        if user_input == result:
            self._check = True
            print("Correct answer! Well done.")
        else:
            print(f"Incorrect. The correct answer is {result}.")
        
    
    def check_correct_answer(self):
        return self._check
    
    
#Polymorphism
list_of_games = []
for _ in range(5):
    list_of_games.append(Hangman('Hangman game'))
    
for _ in range(5):
    list_of_games.append(MathGame('Math game'))
    
random.shuffle(list_of_games)
your_score = 0
for game in list_of_games: 
    game.play()
    if game.check_correct_answer():
        your_score += 1
        
print(f'Your score is {your_score}/10')

           