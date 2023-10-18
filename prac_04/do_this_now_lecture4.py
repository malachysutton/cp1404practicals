# names = ["tom", "bob", "dave", "steve", "tim"]
# number_wanted = int(input("Which number name would you like? "))
# print(names[number_wanted])

names = ["tom", "bob", "dave", "steve", "tim"]
number_delete = int(input("Which number name would you like? "))
del names[number_delete]
print([names])