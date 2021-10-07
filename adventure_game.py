import time
backpack = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

name = input("Before we begin, please enter your name \n")
print_pause("Hello " + name + ", Its nice to meet you !")

teamname = input("Also, can you please make up a name of a sports team? \n")
print_pause (teamname + "...Sounds like a solid team!")


while True: 
    print_pause("You wake up in an empty room. ")
    print_pause("2 doors lie in front of you. Which door will you take?")
    if "baseball bat" and "baseball glove" in backpack:
            print_pause("Oh? Whats this? A Mysterious 3rd door has opened!!??")
            answer = input("Would you like to enter? Enter 'Yes' or 'No' \n").lower
            if answer == "yes":
                print_pause("You walk thru door 3, there's a light at the end of this dark, narrow corridor")
                print_pause("You grasp you bat and glove, unsure of what you will see at the end of the tunnel")
                print_pause("As you approach the light at the end, you hear faint cheers and a chant. It almost sounds like...")
                print_pause("And when you step out into the blinding lights, the chants become clear..") 
                print_pause(name + "!" + name + "!" + name +"!")
                print_pause("The crowd goes wild! They welcome you as the newest member of the " + teamname + "!!!")
                print_pause("THE END, thank you for playing " + name + "!!")
                break
            
            elif answer == "no":
                print_pause("Alright then, suit yourself...")

    door = input("Enter '1' for Door 1 and '2' for Door 2 \n")
    
    if door == '1':
        print_pause("You open door 1, a bright light envelops you.")
        print_pause("You're transported to a suburban neighborhood. You notice a baseball bat lying on the sidewalk")
        if "baseball bat" in backpack:
            print_pause("Ah, seems like you already have one. Just leave it here")
        
        else:
            print_pause("You add it to your backpack")
            backpack.append("baseball bat")


    elif door == '2':
        print_pause("You open door 2, a bright light envelops you..")
        print_pause("You're transported to a bustling, yet unfamiliar cityscape. A man with his fists up approaches you ")
        
        if "baseball glove" in backpack:
            print_pause("Hmmm, seems like you already have what you need from this guy")
            print_pause("Might as well leave him alone and turn around..")
            continue
        
        action = input("What will you do? Fight, or Run? \n").lower()

        if action == "fight":
            
            if "baseball bat" in backpack:
                print_pause("The man swings madly on you, but you deflect his punches with you handy baseball bat")
                print_pause("As he lunges toward you, you lightly tap him with your bat, rendering him unconscious")
                print_pause("The nameless man falls to the ground. Oh? Looks like he droppd something. ")
                print_pause("A baseball glove? Might as well take it.")
                backpack.append("baseball glove")
            
            else:
                print_pause("The man swings madly at you, but you dont have anything but your bare hands to deflect his punches")
                print_pause("You proceed to get the brakes beaten off you. ")
                print_pause("You then proceed to escape by the skin of your teeth. ")
                print_pause("Gee, if only there was something you could could use to defeat him. ")
                print_pause("Perhaps you should check room 1...")
        elif action == "run":
            print_pause("You close your eyes and run in the opposite direction in hopes of returning to where you came from...")
        else:
            print_pause("Sorry, I don't understand...")