def main():
    # f = open('textfile.txt', 'w+')
    f = open('textfile.txt', 'a')

    # for i in range(10):
    #     f.write('This is line ' + str(i) + '\r\n')
    #
    # f.close()
    if f.mode == 'r':
        contents = f.read()
        print(contents)


if __name__ == '__main__':
    main()
