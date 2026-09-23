'''multiple'''
def main():
    'mult'

    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    r = n1 * n2

    print(f"{n1} x {n2} = {r}")

    if r > 0:
            print("This number is positive.")
    elif r < 0:
            print("This number is negative.")
    else:
            print("This number is both positive and negative.")

main()
