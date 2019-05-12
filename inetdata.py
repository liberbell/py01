import urllib.request

def main():
    weburl = 'https://www.google.com'
    result = urllib.request.urlopen(weburl)

    print('Result code: ' + str(result.getcode()))
    data = result.read()
    print(data)

if __name__ == '__main__':
    main()
