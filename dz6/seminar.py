from sem6 import *


def main():
    a =timeout_2.quess_game(guesses=3, bot=1, top=10)
    b = timeout_6.full_game()
    print(a,b,sep="\n")

if __name__ == '__main__':
    main()
