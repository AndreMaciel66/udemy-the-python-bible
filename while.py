L = []

while len(L) <3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry, list is full!")
print(L)

print(type(L))
