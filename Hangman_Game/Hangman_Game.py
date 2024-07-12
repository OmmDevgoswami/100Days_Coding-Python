import random
from Hangman_Art import logo, stages
from Hangman_Words import Word_list

print (logo)
word_at_random = random.choice(Word_list)

ans_list = []
wrong = []
for i in word_at_random:
    ans_list.append("_")
number_of_lives = 6    
    
x = 1
while x == 1:   
    guess_a_letter = input("Make a Guess: ")
    guess_a_letter = guess_a_letter.lower()

    if guess_a_letter in ans_list:
        print (f"You guessed {guess_a_letter}, it's already guessed.")
    
    for i,n in enumerate(word_at_random):
        if n == guess_a_letter:
            ans_list[i] = guess_a_letter
            print ("Congratulations !! You got a correct letter !!")
    # for i in range(0, len(word_at_random)):
    #     if word_at_random[i] == guess_a_letter:
    #         ans_list[i] = guess_a_letter
    
    if guess_a_letter not in word_at_random:
        if guess_a_letter in wrong:
            print (f"It was a repeated wrong guess, you didn't lose a life.")
        elif number_of_lives == 3:
            print ("You have used Half of the Total lives.")
            hint_ran = random.randint(0, len(word_at_random)-1)
            hint = word_at_random[hint_ran]
            if hint not in ans_list:
                print (f"Here's a Hint: {hint}")
            number_of_lives -= 1
        else:
            print (f"You have {number_of_lives} lives left.")
            print (stages[number_of_lives])
            number_of_lives -= 1
            if number_of_lives == -1:
                print ("You Lose")
                print (f"The Correct Word was: {word_at_random}")
                x = 0
        wrong.append(guess_a_letter)
    
    print(ans_list)
    print()

    if "_" not in ans_list:
        print ("You Win !!")
        x = 0
    
    
        
