'''
algorithm:
1. ask computer and user  to choose 4 digit random number.
2 ask user to whom to start the game.

    take a guess from chosen person (either from computer or user)
    
3. run loop through
    if computer guessed:
                user should give two inputs :
                input 1: how many digits are correct from users sceret number, if input is zero dont ask second input
                input 2: is any index correct
            then ask user to guess
    if user guessed:
                computer should give two outputs :
                output 1: how many digits are correct from computers sceret number,if no correct digit rreturn no correct digit.
                output 2: any digit at correct index,if no return no digit at correct index and if no correct digit return no correct digit
            then ask computer to guess
4. loop 3 runs until computer or user guess correct number of others
5.if any one guesses game over exit
'''
import random
from itertools import permutations

def generate_sceret( ):
    return ''.join(random.sample('0123456789',4))
def user_guess( ):
    while True:
        guess = input("Enter a 4 digit number(no repeat):")
        if guess.isdigit( ) and len(guess) == 4 and len(set(guess)) ==4:
                    return guess
        else:
            print("Invalid number.Try again")

def filter_candidates(possible_numbers, last_guess, correct, correct_indices):
    new_candidates = []
    for candidate in possible_numbers:
        c_digits = sum(1 for d in last_guess if d in candidate)
        c_indices = [i for i in range(4) if last_guess[i] == candidate[i]]
        if c_digits == correct and c_indices == correct_indices:
            new_candidates.append(candidate)
    return new_candidates

def check_correct(guess,cmp_sceret):
    crt_digits = sum(1 for d in guess if d in cmp_sceret)
    crt_index = [ i for i in range(4) if guess[i] == cmp_sceret[i] ]
    
    return crt_digits, crt_index


def main():
    print("🎮 Welcome to the 4-digit Number Guessing Game!")
    print("🧠 User, think of a secret 4-digit number (do NOT type it in).")
    print("💻 Computer has chosen its secret number.")

    computer_sceret = generate_sceret()
    all_candidates = [''.join(p) for p in permutations('0123456789', 4)]
    possible_numbers = all_candidates.copy()
    computer_guesses = [ ]

     
    turn = input("Who starts first? Type 'user' or 'computer': ").strip().lower()
    while turn not in ['user', 'computer']:
        turn = input("Invalid choice. Enter 'user' or 'computer': ").strip().lower()

    round_num = 1
    

    while True:
        print( "Round",round_num)
        round_num +=1
        flag =0


        if turn == 'user':
            guess = user_guess()

            correct,crt_index = check_correct(guess,computer_sceret)
            if correct == 0:
                print(" No correct digits")
            else:
                print(f"{correct} digit(s) are correct")
            #if crt_index :
                print(f"✅ Correct digit(s) at index/indices: {crt_index}")
            #else:
                #print("⚠️ None of the correct digits are in the correct position.")

            if correct == 4:
                if guess == computer_sceret:
                    print(" You guessed the computer's number! You win!")
                    flag =0
                    break
            turn = 'computer'
        else:   #computers turn
            guess = random.choice(possible_numbers)
            computer_guesses.append(guess)
            print(f"🤖 Computer guesses: {guess}")

            try:
                correct = int(input("🧠 How many digits are correct? (0-4): "))
                if correct > 0:
                    index_input = input("Enter correct index positions (e.g., 0 2): ")
                    if index_input.lower() == "none" or index_input == "":
                        correct_indices = []
                    else:
                        correct_indices = list(map(int, index_input.split()))
                else:
                    correct_indices = []
                    
            except:
                print("⚠️ Invalid input. Try again.")
                continue

            if correct == 4 and sorted(correct_indices) == [0, 1, 2, 3]:
                print(f"🤖 Computer guessed your number: {guess}")
                print("💻 Computer wins!")
                flag = 1
                break


            possible_numbers = filter_candidates(possible_numbers, guess, correct, correct_indices)
            if not possible_numbers:
                print("❌ No candidates left. Check if previous feedback had errors.")
                break


            turn = 'user'

    
    if flag == 1:
        print(f"you lost to guess {computer_sceret} .Try again")
    else:
        user_no = input("what is the number:")
        print("I lost to guess ",user_no)
    print("Game over")
if __name__ == "__main__":
    main()
