name = input("Type your name: ")
print("Welcome", name, "to this amazing amd fantastical adventure!")

answer = input("You are on a jounrey to see and explore the lands between. A vast and beautful place filled with wonder and mystery. You come to a fork in the road you were on, so which way are you choosing left or right? ").lower()


if answer == "left":
    answer = input("You decide to go left and in the distance you see a small village, do you contiune walking or go into the village? Type continue to go into the village or wander to stay on this winding path: ")

    if answer == "continue":
        print("You treak onwards to the village but upon entering the village you notice that something is wrong its quiet and desolite. Not a living, breathing soul in sight, you investage futher in and find a hord of the undead and then was eaten alive joinig their ranks.")
    else:
        print('Not a valid option. Am sorry but your soul has been sent to the great beyond.')

elif answer == "right":
    answer = input("You take the path to the right and contiune walking up a mountainess path. The wind sundenly picks up forcing you to treak up the mountain faster. You make it too the top of the mountain and see a place to take shelter. Do you take shelter or continue running in search of a better one (take shelter/ continue on)? ")

    if answer == "take shelter":
        print("You go head first into this rundown house to hide from the this indecisve weather. But this shed wasnt actually human but a mimic and you just walked right into its mouth and perished.")
    elif answer == "continue on":
        answer = input("You continue walking on unware that a this wind is slowly kiiling you. But by chance you find shelter but a stranger is also there. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You strike up a nice conersation and the strager introduces himself as Gale a wandering wizard. As the conversation goes on he offers to help show you more of this world and join your ever growing party. Your story shall not end here but will continue to unfold in the Lands Between.")
        elif answer == "no":
            print("You ignore this strangely dress person and they are offended and you lose the game.")
        else:
            print('Not a valid option. Am sorry but your soul has been sent to the great beyond.')  
    else:
        print('Not a valid option. Am sorry but your soul has been sent to the great beyond.')
else:
    print('Not a valid option. Am sorry but your soul has been sent to the great beyond.')

print("Thank you for trying the game", name)