#Task 1: Code Correction 


place = input("Choose a place: forest or cave? ")

if place == "forest":    #Changed = to == in all if conditions
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":     #Changed else action to elif action
        print("You found a boat!")
elif place == "cave":    
    print("You find a hidden treasure!")




#Task 2: Setting the Scene
    

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("You can see your way clearly. You found a chest full of treasures!")
    elif cave_action == "proceed in the dark":
        print("You stumbled upon a hidden trap and fell into a pit. Game over!")




#Task 3: Default Path
        

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  #Unknown
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("You can see your way clearly. You found a chest full of treasures!")
    elif cave_action == "proceed in the dark":
        print("You stumbled upon a hidden trap and fell into a pit. Game over!")
    else:
        pass  #Unknown
else:
    pass  #Unknwon
