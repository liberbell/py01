def main():
    x, y = 1000, 100

    if (x < y):
        st = "X is less than Y"
    elif (x > y):
        st = "X is greater than Y"
    else:
        st = "X equal Y"

    print(st)

    st = 'X is less than Y' if (x < y) else 'X is greater than or same as Y'
    print(st)

if __name__ == '__main__':
    main()
