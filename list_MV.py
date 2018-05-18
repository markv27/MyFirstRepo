name = "Mark Vollmer"

subjects = ["English","Math","Chinese","Science","History"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)
    

characters = ["Luke","Han","Vader","Chewy","Leia"]
for i in characters:
    if i == "Vader":
        print(i + " is the villan in Star Wars")
    elif i == "Luke":
        print(i + " is the protagonist in Star Wars")
    elif i == "Han":
        print(i + " is the best pilot in the galaxy")
    else:
        print("One of the best characters in Star Wars is " + i)
          


sports = []

while True:
    print("What's your favorite sport? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        sports.append(answer)

for i in sports:
    print("One of your favorite sports is " + i)
