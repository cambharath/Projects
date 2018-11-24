import json
import csv
import requests
import time

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=12.9538477,77.3507442&radius=20000&type=atm&key=YOURKEY'

headers={'content-type':'application/json',
         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0'}


def csv_write():
    csvfile =open('google_maps.csv','w')
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["name","lat","long"])

    response = requests.get(url=url, headers=headers).json()
    for obj in response['results']:
        writer.writerow ([obj['name'],obj['geometry']['location']['lat'],obj['geometry']['location']['lng']])

    print ('next_page_token' in response)
    while 'next_page_token' in response:
        URL = url + '&pagetoken=' + response['next_page_token']
        time.sleep(5)
        response = requests.get(url=url, headers=headers).json()
        for obj in response['results']:
            writer.writerow ([obj['name'],obj['geometry']['location']['lat'],obj['geometry']['location']['lng']])

    else:
        print(response)


if __name__ == '__main__':
    csv_write()


