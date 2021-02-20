secret_word= "jatin"
guess= ""
guess_count = 0
guess_limit = 4
out_of_guesses = False
score = 0

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess= input("enter your guess")
        guess_count + 1
    else:
        out_of_guesses= True

if out_of_guesses:
    print("you lose")
else:
    print("you win" )
