import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#second solution
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
password2 = ""
for char in password_list:
    password2 += char
print(password2)

# first solution
list1 = [letters, symbols, numbers]
password = ""
while nr_numbers+nr_symbols+nr_letters != 0:
    i = random.randint(0,2)
    if i == 0 and nr_letters > 0:
        password = password + list1[i][random.randint(0, len(list1[i]) - 1)]
        nr_letters -= 1
    elif i == 1 and nr_symbols > 0:
        password = password + list1[i][random.randint(0, len(list1[i]) - 1)]
        nr_symbols -= 1
    elif i == 2 and nr_numbers > 0:
        password = password + list1[i][random.randint(0, len(list1[i]) - 1)]
        nr_numbers -= 1
print(password)
