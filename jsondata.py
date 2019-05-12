# from urllib import request
import urllib.request
import json

def printResults(data):
    theJson = json.loads()

def main():
    urlData = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson'

    weburl = urllib.request.urlopen(urlData)
    print('Result code: ' + str(weburl.getcode()))

if __name__ == '__main__':
    main()
