from colorama import Fore, Back, Style

cat_dict = {}
  
print(Fore.CYAN+" Let's make virtual cat. \n We need some more information like name, age, weight \n\n")
name = input(Fore.GREEN+"Name of the pet :")
age = input(Fore.GREEN+"Age of the pet :")
weight = input(Fore.GREEN+"Weight of the pet :")

cat_dict["Name"]=name
cat_dict["Age"] = age
cat_dict["Weight"] = weight
cat_dict["Hungry"] = True
cat_dict["Photo"] = "≧◔◡◔≦"

print(Back.CYAN+"\n\n***********************************************")
print(Back.RESET)
for x,y in cat_dict.items():
  print(Fore.RED+ x,":"+str(y))


