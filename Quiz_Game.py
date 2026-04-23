def new_game():

    guesses = []
    correct_guesses = 0
    questions_num = 1 # quest num is 1 so the 2 quest in dic

    for key in questions: #key in quest dic
        print("-----------------------------")
        print(key)
        for i in options[questions_num-1]: #index value of options list for quest -1 means 0 the first quest print 0 postion in list
            print(i)
        guess = input("Enter (A, B, C, or D): ") #giving input as value
        guess = guess.upper() #convert the input to upper
        guesses.append(guess) #add the guess in guesses variable

        correct_guesses += check_answer(questions.get(key), guess) #keep adding the value for each crt ans and guess
        questions_num += 1 #keep show and add value for quest

    display_score(correct_guesses, guesses) #show the result of crt guess and guess

#----------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
#----------------------
def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")

    print("ANSWERS: ", end=" ")
    for i in questions: #key value in quest
        print(questions.get(i), end=" ") #i means key values in dic
    print()

    print("GUESSES: ", end=" ")
    for i in guesses: #given input by player in guesses
        print(i,end=" ")
    print()

    score = int((correct_guesses/len(questions))*100) #convert ans values 4/4 * 100 the first 4 is crt input of user
    print("Your Score is : "+str(score)+"%") #print converted value with %

#----------------------
def play_again():
    response = input("Do you want to play again (Yes or No): ")
    response = response.upper()

    if response == "YES":
        return True #return to start
    else:
        return False #end the game
#-----------------------

questions = {
    "Who created Python? :":"A",
    "What year was Python Created? :":"B",
    "Python is tributed to which comedy group? :":"C",
    "Is the Earth round? :":"A"
}

options = [["A. Guldo van Rossum","B. Elon Musk","C. Bill Gates","D. Mark Zuckerburg"],
           ["A. 1989","B. 1991","C. 2000","D. 2018"],
           ["A. Lonely Island","B. Smosh","C. Monty Python","D. SNL"],
           ["A. True","B. False","C. sometimes","D. What's Earth?!"]]

new_game()

while play_again(): #while loop for keep playing
    new_game()

print("Byeeeeee!")
