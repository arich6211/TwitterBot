#This will post the current coordinate location of the ISS based on Open Notify API
import sys
from twython import Twython
import json
import turtle
#Python 2: urllib2 / Python 3: urllib3
import urllib2

url = 'http://api.open-notify.org/iss-now.json'

response = urllib2.urlopen(url)
result = json.loads(response.read()
location = result['iss_position']
lat = (location['latitude'])
lon = (location['longitude'])

tweetStr = 'The ISS current longitude/latitude is: ' + lon + ' & ' + lat

apiKey = 
apiSecret = 
accessToken = 
accessTokenSecret = 

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
