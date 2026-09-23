'''multiplication_table'''
def main():
    '''table'''

    n = int(input("Enter a number\n"))

    for i in range(13):
        print(f"{i} x {n} = {i * n}")

main()
