#Michael McGrail
#Introduction to Programming
#Lab 5

animal = "snake"

def main():
    print("I am thinking of an animal...")
    guess = input("What am I thinking of? ")
    guess = guess.lower()
    correct = False
    while not correct:
        if guess[0] == 'q':
            quit(0)
        elif guess != 'snake':
            print ("Wrong answer! Guess again.")
            guess = input("What am I thinking of? ")
            guess = guess.lower()
        else:
            print ("Congratulations! You got it!")
            follow_up = input("Do you like snakes?? ('y' or 'n') ")
            if follow_up == "y":
                print ("I thought of something you like!")
            else:
                print ("I thought of the wrong animal")
            return

main()
