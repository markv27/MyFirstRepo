import pyautogui as pg
import time

points = 0

# Question
answer = pg.prompt(
"""
Which would you rather do?

a) Go skiing
b) Sunbathe at the beach
c) Touring an American city


"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer = pg.prompt(
"""
What type of weather do you prefer

a) Cool - 50 or less
b) Warm - 70+
c) Medium - 50-70


"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer = pg.prompt(
"""
What type of resort are you looking for?

a) Out early - home late
b) At the resort the whole day
c) Leave in the late morning - home for dinner


"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer = pg.prompt(
"""
What area of the country do you prefer?

a) Mountains
b) West Coast
c) Urban Areas


"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# END OF SURVEY
pg.alert("You are going to...")

#Deer Valley Vacation
if points >3 and points <=6:
    pg.alert("A Luxury Ski Vacation, Montage Deer Valley")
#Beverly Hills
if points >6 and points <=9:
    pg.alert("An Outstading Beach Resort Stay in Beverly Hills")
#New York City
if points >10:
    pg.alert("NYC for a tour of the Big Apple")
    
