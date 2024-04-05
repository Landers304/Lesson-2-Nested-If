#Task 1: Code Correction


attendees = int(input("Enter number of attendees: "))    #Added Int before the input
venue = "large hall" if attendees > 100 else "conference room"
print(venue)




#Task 2: Venue Selection 
#Needed further research of lists to complete this assignment, Took much longer than expected
#Learned append, insert and join method when adding elements to a list

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
facilities = []

if attendees > 50:
    facilities.append("audio system")     
if attendees > 80:
    facilities.append("projector")

print("Venue:", venue)
if facilities:
    print("Additional facilities recommended:", ", ".join(facilities))
else:
    print("No additional facilities recommended.")




#Task 3: catering Choices
    

vegetarian_choice = input("Do you want vegetarian food? (yes/no): ")

if vegetarian_choice == "yes":
    print("We recommend Veggie Delight Caterers for vegetarian options.")
else:
    print("We recommend Gourmet Meals Caterers for non-vegetarian options.")


