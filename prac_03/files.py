# name_file = open("name_file.txt", "w")
#
# name = input("What's the name? ")
# print(f"{name}", file=name_file)
#
# name_file.close()


name_file = open("name_file.txt", "w")

name = input("What's the name? ")
print(f"Your name is {name}", file=name_file)

name_file.close()