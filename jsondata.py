# from urllib import request
import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    if 'title' in thJSON['metadata']:
        print(theJSON['metadata']['title'])

    count = theJSON['metadata']['count']
    print(str(count) + ' events recorded.')

def main():
    urlData = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson'

    weburl = urllib.request.urlopen(urlData)
    print('Result code: ' + str(weburl.getcode()))
    if (weburl.getcode() == 200):
        data = weburl.read()
        printResults(data)
    else:
        print('Received error, cannot parse results.')

if __name__ == '__main__':
    main()
