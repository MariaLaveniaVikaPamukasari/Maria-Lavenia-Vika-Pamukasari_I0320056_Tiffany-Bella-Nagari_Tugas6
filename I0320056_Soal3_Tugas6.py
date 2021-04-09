print(" ")
print("\t\t\tProgram pengecekan bilangan prima")
print(" ")

for a in range(10, 25):
    if a == 10:
        print(a, "bukan prima")
    elif a == 11:
        print(a, "adalah bilangan prima")
    else:
        for i in range(2, a):
            if a % i == 0:
                print(a, "bukan prima")
                break
        else:
            print(a, "adalah bilangan prima")