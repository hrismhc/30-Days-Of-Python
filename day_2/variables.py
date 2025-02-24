import math

first_name, last_name, space = "haris", "mehic", " "
full_name = first_name + space  + last_name
country = "germany"
city = "stuttgart"
age = 20 
year = 2004
is_married = False 
is_true = True
is_light_on = False

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name), len(last_name)) 

num_one, num_two = 5, 4

total = num_one + num_two

diff = num_one - num_two

product = num_one * num_two

division = num_one / num_two

remainder = num_one % num_two

exp = num_one ** num_two

flor_division = num_one // num_two

radius =  int(input("radius of circle: "))

area_of_cicle = round(math.pi * radius**2, 2)

circum_of_cirlce = round(2 * radius * math.pi, 2)

print("Area of circle :", area_of_cicle, "Cicum of the circle ", circum_of_cirlce)
