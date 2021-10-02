import urllib, json
import random
import time
from secrets import (cellphone, twilio_account_sid, twilio_number,
                        twilio_token)
import requests
import schedule 
from twilio.rest import Client

#Fetch Quote from They Said So API, Limited to 10 API calls per day for free Public API. 
url = 'https://quotes.rest/qod'
headers = {'content-type': 'application/json'}
response = requests.get(url, headers=headers)
quotes = response.json()['contents']['quotes'][0].values()# We fetch the quote from the returned JSON,
                                                          # under the "quote" header. See the They Said
                                                          # So API for more details on how JSON is formatted. 

DAILY_QUOTE = quotes 


#Send the Daily Quotes Message 
def send_message(quotes_list=DAILY_QUOTE):

    account = twilio_account_sid
    token = twilio_token          
    client = Client(account, token) #Twilio User/Client Authentication 

    message = client.messages.create(to=cellphone,
                           from_= twilio_number,
                           body = quotes_list,
                           )

    print(message.sid) #String identifier (i.e  "SM2862ab260eac49fd99d8e915dd2dbb69") will be printed if successful. 

#Scheduling the message

#Send every day at this specified time in the brackets. 
schedule.every().day.at("10:58").do(send_message, DAILY_QUOTE)

#Test option to send the message NOW. Change time in the brackets to NOW.  
schedule.every().day.at("12:54").do(send_message, DAILY_QUOTE)

#This loop is used to check if any scheduled tasks are still pending. 
while True:
    schedule.run_pending()
    time.sleep(2)
