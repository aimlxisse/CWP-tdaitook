def main():
    num = float(input("Give me a number: "))

    if num % 1 > 0:
        result = int(round(num + 0.5))
    else:
        result = int(num)

    print(result)

main()