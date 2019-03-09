films = {
    "Finding Dory":[3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("What film do you want to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        # check user age        
        if age >= films[choice][0]:
            
            # check enough seats
            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
                
        else:
            print("You're too young to see the film!")
        
    else:
        print("We don't have that film...")
