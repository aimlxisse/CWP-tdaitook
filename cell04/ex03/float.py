def main():
    n = input("Give me a number: ")

    number = float(n)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
        
main()