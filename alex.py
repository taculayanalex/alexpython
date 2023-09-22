# A B C D E AND F ALGORITHM I DONT SURE IF ITS ALGORITHM HAHAHAHAHA ^_^
a = 33
b = 34 
if b > a:
    print(" b is greater than a !")
c = 33 
d = 33 
if c > d:
    print("c is greater than d ! ")
elif c == d:
    print(" c and d are equal ! ")
e = 2023
g = 2005
if e > g:
    print(" g is greater than e !")
elif e == g:
    print(" e and g are equal ! ")
else:
    print(" e is greater than g ! ")
course = 'INFORMATION SYSTEM !'
print(course)

# FALSE ELSE AND LOOP ! 

successful = False
for number in range (5):
    print("Attempt")
    if successful:
        print(successful)
        break
else:
    print("NOT SUCCESSFUL ATTEMPT 3 TIMES AND FAILED !")

# TRUE ELSE AND LOOP ! 

successful = True
for number in range (3):
    print("Attempt")
    if successful:
        print(successful)
        break 
else:
    print("NOT SUCCESSFUL ATTEMP 3 TIMES AND FAILED !!!")

# LOOPS !!!!!!!!!!
# THIS OF CODES CONTINUE TO COUNT 1 TO 20 BEACUSE IS CONTINUE
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
# AND FOR BREAK 1 TO 20 IT WILL BREAK BEACUSE OF THE IF x == 13 and then break

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
# WHILE LOOP NAME AND AGE !!!!!!!!!!!!!!!!!!!!!!!

name = input ("Enter your name: ")

while name == "":
    print("You did not enter your name ")
    name = input ("Enter your name: ")
print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be a negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old !")

#WHILE LOOP EXECUTE SOME CODE WHILE SOME CONDITION REMAINS TRUE 

num = int(input("Enter a # 1 - 100: "))

while num < 1 or num > 100:
    print(f"{num} is not valid")
    num = int(input("Enter a # 1 - 100: "))

print(f"Your number is {num}")


