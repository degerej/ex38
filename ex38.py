# Joe Degere
# 11/6/2019
# Doing Things To Lists


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that last list. Let's fix it.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # Whoa! fancy
print(stuff.pop())
print(''.join(stuff))  # What? cool!
print('#'.join(stuff[3]))  # Super cool!
