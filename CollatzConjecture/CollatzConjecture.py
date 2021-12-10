def collatz_conjecture(x):
    x = int(x)
    if x % 2 == 0:
        x //= 2
    else:
        x = x * 3 + 1
    return x


def print_collatz(x):
    print("Collatz conjecture for " + x + " is:")
    print(collatz_conjecture(x))
    y = 0
    while collatz_conjecture(x) > 1:
        x = collatz_conjecture(x)
        print(collatz_conjecture(x))
        y += 1
    else:
        if collatz_conjecture(x) == 1:
            y += 1
            if y > 1:

                print("The number satisfies Collatz Conjecture")
                print("It reaches 1 after " + str(y) + " steps")
            else:
                print("The number satisfies Collatz Conjecture")
                print("It reaches 1 after 1 step")
        else:
            print("The number does not satisfy Collatz Conjecture")


def print_intro():
    print("The Collatz Conjecture:")
    print(
        " The collatz conjecture states that any natural number eventually reaches 1 after several steps such that each"
        " term is obtained from the previous term as follows: ")
    print("            If the term is even, the next term is one half of the term.")
    print("            If the term is odd, the next term is 3 times the term plus 1.")
    print("To check if your number satisfies Collatz Conjecture")


print_intro()
n = input("Enter a number:")
i = 1
while i > 0:

    if n.isdigit() and int(n) > 1:
        print_collatz(n)
        break
    elif n == "1" and n.isdigit():
        print("Please enter a number other than 1")
        n = input("Enter a number: ")
    else:
        print("Invalid character")
        n = input("Enter a valid number: ")
