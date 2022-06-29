from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os 

# Account SID and Auth Token from www.twilio.com/console
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
app = Flask(__name__)


# A route to respond to SMS messages
@app.route('/sms', methods=['POST', 'GET'])
def inbound_sms():

    body = request.values.get('Body', None)

    response = MessagingResponse()
    with open('quotes_shuffled.txt') as f:
        lines = f.read()
        myarray = lines.split("\n\n")
    
    print("here")
    try:
        int(body)
    except:
        response.message(f"Please enter a number between 1 and {len(myarray)}")
        return str(response)
    
    print(myarray[int(body)])
    response.message(myarray[int(body)])

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)