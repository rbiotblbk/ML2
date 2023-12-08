

def greeting(name):
    print(f"Hallo, {name} ")

def add(x ,y ):
    print("X:", x)
    print("Y:", y)
    total = x + y 
    #print("test: ", total )
    total = round(total ,2)

    return total 

def mwst(number ):

    print("test", number)
    total = number * 1.19
    

   # print("test with mwst", total)
    return total 



def main():
    greeting("Thomas") 

    total = add("apfel",4)
    print(total)

    total_mwst = mwst(total)
    print(total_mwst)

if __name__ == "__main__":
    main()



