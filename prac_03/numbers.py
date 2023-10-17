number_file = open("numbers.txt", "r")
first_number=number_file.readline(1)
second_number=number_file.readline(2)
result = first_number * second_number
print(result)
number_file.close()
