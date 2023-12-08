

location = "Berlin"


def greeting1(name):
    print("Hallo", name, location) # global value -- read only


def greeting2(name):
    location = "Frankfurt" # creates a new local variable
    print("Hallo", name, location)


def greeting3(name):
    global location # make the global variable writable

    location = "Stuttgart" # change the global value 
    print("Hallo", name, location)




greeting1("Thomas")


greeting2("Sven")

greeting3("Olha")

print(location)