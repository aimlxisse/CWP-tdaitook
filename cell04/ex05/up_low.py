''' up_low'''
def main():
    '''main'''

    n = input()
    r = ""

    for i in n:
        if i == i.lower():
            r += i.upper()
        else:
            r += i.lower()
    print(r)
    
main()