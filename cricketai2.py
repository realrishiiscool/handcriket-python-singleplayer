import random as rd

#function to keep track of score and bat ball one of them is randmizer
def playcricket(player1roll, name):
    score1 = 0
    score2 = 0
    #if the user chooses bat or ai chooses to ball
    if player1roll == "bat":
        ball = 1
        bat = 0
        print(f"{name}'s turn to bat.")

        while bat != ball:
            ball = rd.randint(1, 10)
            bat = int(input(f"Score={score1} Enter your roll (1 to 10 number only): "))
            if bat > 10:
                print("Retoss your coin.. don't break the rules..")
                exit()
                #code stop if number is out of bound
            print(f"AI Bob's roll: {ball}")
            if bat != ball:
                score1 += bat
            print(f"{name}'s score: {score1}")

        print(f"{name} is out!")
        print("AI Bob's turn to bat.")

        ball = 1
        bat = 0
        #condition are vice versa while caluculating logic is same
        #only differece we give input first or the bat(ai) or else we can see the ball then its chetable
        while bat != ball:
            ball = rd.randint(1, 10)
            bat = int(input(f"Score={score2} Enter your roll (1 to 10 number only): "))
            if bat > 10:
                print("Retoss your coin.. don't break the rules..")
                exit()
            print(f"AI Bob's roll: {ball}")
            if bat != ball:
                score2 += bat
            print(f"AI Bob's score: {score2}")

        print("AI Bob is out!")
        #finally to showcase the score
        if score1 > score2:
            print(f"{name} wins!")
        elif score2 > score1:
            print("AI Bob wins!")
        else:
            print("It's a tie!")
    #if the user chooses ball same but small adjustment according to ball
    elif player1roll == "ball":
        ball = 1
        bat = 0
        print("AI Bob's turn to bat first.")

        while bat != ball:
            ball = int(input(f"Score={score1} Enter your roll (1 to 10 number only): "))
            bat = rd.randint(1, 10)
            print(f"AI Bob's roll: {bat}")
            if bat != ball:
                score1 += bat
            print(f"AI Bob's score: {score1}")
            if ball > 10:
                print("Retoss your coin.. don't break the rules..")
                exit()

        print("AI Bob is out!")
        print(f"{name}'s turn to bat.")

        ball = 1
        bat = 0
        while bat != ball:
            ball = rd.randint(1, 10)
            bat = int(input(f"Score={score2} Enter your roll (1 to 10 number only): "))
            if bat > 10:
                print("Retoss your coin.. don't break the rules..")
                exit()
            print(f"AI Bob's roll: {ball}")
            if bat != ball:
                score2 += bat
            print(f"{name}'s score: {score2}")

        print(f"{name} is out!")

        if score2 > score1:
            print(f"{name} wins!")
        elif score1 > score2:
            print("AI Bob wins!")
        else:
            print("It's a tie!")


def choosetoplay():
    ai = rd.randint(1, 2)
    coin = rd.randint(1, 2)
    name = input("Enter your name: ").strip()
    choice = input("Select 'head' or 'tails': ").strip().lower()
    print("Toss result:", "Heads" if ai == 1 else "Tails")

    if choice == "head" or choice == "tails":
        if (choice == "head" and coin == 1) or (choice == "tails" and coin == 2):
            player1roll = input("It's your lucky day! Your choice for bat or ball: ").strip().lower()
            if player1roll not in ["bat", "ball"]:
                print("Invalid choice. Defaulting to bat.")
                player1roll = "bat"
            playcricket(player1roll, name)
        else:
            print("The coin landed on the opposite side.")
            l = ["bat", "ball"]

            choice = rd.choice(l)
            print("AI Bob:according to my computation i am gonna choose ", choice)
            if choice == "bat":
                playcricket("ball", name)
            elif choice == "ball":
                playcricket("bat", name)
    else:
        print("Invalid choice for the toss. Please select 'head' or 'tails'.")


# Run the main function
choosetoplay()