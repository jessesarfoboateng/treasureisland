print("Welcome to Treasure Island!\nYour mission is to find the treasure.")
direction = input('You\'re  hat a cross road.Where do you want to go? Type "left" or "right"? ').lower()
if direction.lower() == "right":
    print("Game Over! ")
elif direction.lower() == "left":
    decision_1 = input('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat . Type "swim" to swim across: ''')
    if decision_1.lower() == "swim":
        print("Game Over! ")
    elif decision_1.lower() == "wait":
        decision_2 = input("You arrive at the island unharmed. There is a house with 3 doors.One red,one yellow and one blue. Which colour do you choose? ")
        if decision_2.lower() == "yellow":
            print("You found the treaure. YOU WIN!")
        elif decision_2.lower() == "blue" or "red":
            print("Game over! ")
        else:
            print("Unknown input!")
    else:
        print("Unknown input!")
else:
    print("Unknown input!")



