'''advance table'''
def main():

    i = 0
    j = 0
    while i < 11:
        while j < 11:
            print(f"Table de {j}: {i * j} {i + 1 * j} {i + 2 * j} {i + 3 * j} {i + 4 * j} {i + 5 * j} {i + 6 * j} {i + 7 * j} {i + 8 * j} {i + 9 * j} {i + 10 * j} ")
            j += 1
        i += 1

main()
