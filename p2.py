import random

# ----- Word list (small on purpose) -----
WORDS = [
    "crane", "trace", "slate", "flame", "blame",
    "grape", "plane", "brick", "pride", "shine",
    "stone", "money", "cigar", "reign", "sweet",
    "sound", "round", "heart", "earth", "water"
]


# ----- Core scoring logic -----
def score_guess(guess, secret):
    output = []
    [x for x in secret]
    for i in range(5):
        if guess[i] == secret[i]:
            output.append('Y')
        elif guess[i] in secret:
            output.append('O')
        else:
            output.append('X')
    return ''.join(output)


# ----- Check guess formatting ----- Checks for 5 character all lowercase string
def is_valid_guess(guess: str) -> bool:
    if len(guess) != 5:
        return False
    for i in range(5):
       if ord(guess[i]) < 97 or ord(guess[i]) > 122:
           return False
    return True
    

# ----- Choose secret word ----- Chooses first element of a list of words
def choose_secret(words):
   return words[0]





# ----- One turn of the game -----
def play_turn(secret: str, guess: str) ->str:
    if not is_valid_guess(guess):
        return 'Invalid guess'
    return score_guess(guess, secret)


# ----- Full Wordle game -----
def play_game(words):
    pass


