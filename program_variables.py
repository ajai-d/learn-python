# import date
from datetime import date

# program.py
sum = 1 + 2
print(sum)
# print hurry my first ever python program
print("Hurray! I wrote my first program in python")

product = sum * 2
print(product)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

# type of variable
print("planets_in_solar_syatem is a ",type(planets_in_solar_system))

# type of variable distance_to_alpha_centauri
print("distance_to_alpha_centauri is a ",type(distance_to_alpha_centauri))

# operators

x = 2
# print value of x = x

print("x=2")
print("value of x = ",x)

x += 2
print("x+=2")
print("value of x = ",x)

x -= 2

print("x-=2")
print("value of x = ",x)

x *= 2 

print("x*=2")
print("value of x = ",x)

x /= 2
print("x/=2")
print("value of x = ",x)

x **= 3
print("x**=3")
print("value of x = ",x)

# print today's date with the prefix "Today is "
# use the date.today() function

print("Today is ",date.today()) 
