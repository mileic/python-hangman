#Imports
import time
import sys
import new_try
import console_clear
import gallows

sys.path.append("modules/")
word = input("Enter a word of your choice: ")
word = word.lower()
word_length = len(word)

#Console clear
console_clear.clear()

word_display = []
LIST_COUNTER = 0

for letter in word:
    if LIST_COUNTER <= word_length:
        word_display.append("_")
        LIST_COUNTER = LIST_COUNTER + 1
    else: break
      
print(str(word_display))
print("\n")

FAIL_COUNTER = 0
FAIL_LIMIT = 6

for letter in word:
    TRY_LEFT = FAIL_LIMIT - FAIL_COUNTER
    print("You got "+str(TRY_LEFT)+" wrong try's left.")
    guess = input("Guess a letter: ")
    guess = guess.lower()
 
    if guess in word:
        print("Your guess is correct!\n")
        DIGIT_COUNTER = 0
        DIGIT_COUNTER_REVERSE = 0
        for letter in word:
            if guess == word[DIGIT_COUNTER]:
                word_display[DIGIT_COUNTER] = str(guess)
            else:
                DIGIT_COUNTER = DIGIT_COUNTER + 1
        for letter in word:
            if guess == word[DIGIT_COUNTER_REVERSE]:
                word_display[DIGIT_COUNTER_REVERSE] = str(guess)
            else:
                DIGIT_COUNTER_REVERSE = DIGIT_COUNTER_REVERSE -1
        print(str(word_display)+"\n")

        #Test
        CONTROL_COUNTER = 0
        control = []

        for letter in word:
            control.append(word[CONTROL_COUNTER])
            CONTROL_COUNTER = CONTROL_COUNTER + 1
        if control == word_display:
            print("You win.")
            new_try.again()
        else:
            continue

    else:
        print("Your guess is wrong!")
        FAIL_COUNTER = FAIL_COUNTER + 1

    if FAIL_COUNTER == 1:
        time.sleep(1)
        gallows.gallow_1()
    elif FAIL_COUNTER == 2:
        time.sleep(1)
        gallows.gallow_2()
        time.sleep(1)
    elif FAIL_COUNTER == 3:
        gallows.gallow_3()
    elif FAIL_COUNTER == 4:
        time.sleep(1)
        gallows.gallow_4()
    elif FAIL_COUNTER == 5:
        time.sleep(1)
        gallows.gallow_5()
    elif FAIL_COUNTER == 6:
        time.sleep(1)
        gallows.gallow_6()
        print("You lose.")
        
        #New try?
        new_try.again()
