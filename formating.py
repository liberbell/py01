from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime('The current year is %Y'))
    print(now.strftime('The current month is %b'))
    print(now.strftime('%a, %d %B, %y'))

if __name__ == '__main__':
    main()
