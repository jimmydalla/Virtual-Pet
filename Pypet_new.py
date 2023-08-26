from colorama import Fore, Back, Style

dog_dict={
  "name":"Da Ninja",
  "weight":25,
  "age":2,
  "healthy_weight":27,
  "hungry":False,
  "photo":"ˁ˚ᴥ˚ˀ"
}

# print the details of Ninja
print(Fore.BLUE+"Presenting "+dog_dict["name"]+"...............\n")
print(dog_dict)
print("**********************************")
for x,y in dog_dict.items():
  print(x+":"+str(y))
# for x in dog_dict.values():
#   print(x)


print(Fore.RESET)

# Feeding the pet
# Check whether pet is hungry
# If the pet is hungry , check whether he is overweight.
# If yes, let the user know that 
# Get the user choice for feeding the pet
# If its yes, increase the weight by 0.5, set the hunger status to False and print the updated weight of the pet
#
def feedPet():
  if dog_dict["hungry"]==True:
    if dog_dict["weight"]>dog_dict["healthy_weight"]:
      print(Fore.RED+"\nYour pet, "+dog_dict["name"]+" is already overweight.")
    feed = input("\nYour pet is hungry. Do you want to feed him ? Type Yes or No: ")
    if feed.lower()=="yes":
      dog_dict["weight"]+=0.5;
      dog_dict["hungry"] = False
      print(Fore.BLUE+"\nHurray............., your pet is no more hungry and the current weight is"+str(dog_dict["weight"]))
  else:
    print(Fore.GREEN+"\nYour pet is not hungry")

# To play with the pet

def playwithPet():
  if dog_dict["hungry"]==False:
    print(Fore.CYAN+"\n"+dog_dict["name"]+" enjoyed a lot")
    dog_dict["weight"]-=2.5
    dog_dict["hungry"]=True
  else:
    feedPet()


def petSleep():
  if dog_dict["hungry"]==False:
    print(Fore.CYAN+"\n"+dog_dict["name"]+" wants to sleep. Don't wake him up or else he won't let you sleep")
  else:
    feedPet()

user_ch = "yes"
while user_ch.lower()=="yes":
# actions to be done with the pet
  choice = int((input(Fore.YELLOW+"\nTpye 1 to feed your pet \nType 2 to play with your pet \nType 3 to put your pet to sleep \nType 4 to Exit \nType your choice and enjoy .............. ")))
  if choice == 1:
    feedPet()
  elif choice == 2:
    playwithPet()
  elif choice == 3:
    petSleep()
  elif choice == 4:
    print("Hope you enjoyed spending time with "+dog_dict["name"])
    break
  else:
    print("Oops seems you have entered a wrong choice")  
  user_ch = input(Fore.RED+"\nDo you want to continue. Type Yes or No. ")
else:
  print(Fore.RED+"Hope you enjoyed spending time with "+dog_dict["name"])  

print(Fore.RESET)