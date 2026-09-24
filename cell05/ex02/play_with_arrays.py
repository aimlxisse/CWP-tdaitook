def main():

    original_arrays = [2, 8, 9, 48, 8, 22, -12, 2]
    new_arrays = [x + 2 for x in original_arrays]
    new_arrays2 = []

    for i in new_arrays:
        if i > 5:
            new_arrays2 += [i]
    print(f"{original_arrays}\n{new_arrays2}")

main()
