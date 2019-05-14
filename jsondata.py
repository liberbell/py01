# from urllib import request
import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])

    count = theJSON['metadata']['count']
    print(str(count) + ' events recorded.')

    for i in theJSON['features']:
        print(i['properties']['place'], i['properties']['mag'])
    print('---------\n')

    for i in theJSON['features']:
        if i['properties']['mag'] >= 4.0:
            print('%2.1f' % i['properties']['mag'], i['properties']['place'])

    print('---------\n')

    print('Events that were felt: ')
    for i in theJSON['features']:
        feltReports = i['properties']['felt']
        if feltReports != None:
            if feltReports > 0:
                print('%2.1f' % i['properties']['mag'], i['properties']['place'],
                ' reported ' + str(feltReports) + ' times.')



def main():
    urlData = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'

    weburl = urllib.request.urlopen(urlData)
    print('Result code: ' + str(weburl.getcode()))
    if (weburl.getcode() == 200):
        data = weburl.read()
        printResults(data)
    else:
        print('Received error, cannot parse results.')

if __name__ == '__main__':
    main()
