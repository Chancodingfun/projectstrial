name = input("Type your name: ")
print("Welcome adventurous", name+"! Welcome to this adventure")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input(
        "You have come across a river blocking your way. You can either walk around it or swim across? Type either walk or swim: ").lower()

    if answer == "swim":
        print("You sawm across and got eaten by an alligator.")

    elif answer == "walk":
        input("You walked for miles until you are on a brink of death. While you collapsed ,you saw a shadow giving you water and saving your life. press enter to continue.")
        answer = input("you woke up in a unfamilar house with nobody inside and found an open window beside the bed.You can either run out of the house or wait until someone come back. type in either run or stay: ").lower()

        if answer == "run":
            print(
                "You leg got trapped in a bear trap while jumping off from the window and You bled to dead")

        elif answer == "stay":
            print("A man came back, instead of helping you, he pulled out a Machete and chop you down alive,starting from the limbs and head at last. You died with a painful scream.")

        else:
            print("Not a valid option. You lose")

    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly,do you want to cross it or head back? type cross or back: ").lower()
    if answer == "cross":
        answer = input(
            "You cross the bridge and met a stranger. Do you talk to him (yes/no): ").lower()
        if answer == "yes":
            print("Yoy talk to the stranger and he gave you gold.You win!")

        elif answer == "no":
            print("You ignore the stranger and he is pissed and shot you dead")

        else:
            print("Not a valid option. You lose")

    elif answer == "back":
        input("You go back to tthe main road. Now you can decide to drive to the left or to the right")
        print("Your car crashes on the way and you die")

    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")

print("Thank you for trying", name)
