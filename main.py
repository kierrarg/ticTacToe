import ai as ai

def main():
    while True:
        print("Would you like or play Y/N\n")
        user = input(">>")
        #string handling
        if user.lower() == 'y':
                ai.playVai()
        else:
            print("Thanks for playing")
            exit()

if __name__ == '__main__':
    main()