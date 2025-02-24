import sys
sys.path.append(r"C:\Users\haris\Documents\python_basics\30-Days-Of-Python\data")
from countries import countries 

for x in range(1,11):
    print(x)
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    i = 10

for x in range(10,0,-1):
    print(x)
while i > 0:
    print(i)
    i -= 1

structure = "#"

while len(structure) <= 7:
    print(structure)
    structure += "#"
else:
    structure = "#"

for i in range(8):
    for x in range(8):
        if x != 7:
            print(structure," ", end="")
        else:
            print(structure)

for i in range(11):
    print(i, " x ", i, " = ", i*i)

test_list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in test_list:
    print(i)

for i in range(101):
    if i%2 == 0:
        print(i)

for i in range(101):
    if i%2 != 0:
        print(i)

sum = 0
even_sum = 0
odd_sum = 0

for i in range(101):
    sum += i

print("The sum of all numbers is: ", sum)

for i in range(101):
    if i%2 == 0:
        even_sum += i

print("The sum of all even numbers is: ", even_sum)

for i in range(101):
    if i%2 != 0:
        odd_sum += i

print("The sum of all even numbers is: ", odd_sum)

counries_containing_land = [""];

for i in countries:
    if "land" in i:
        countries.append(i)

print(counries_containing_land)