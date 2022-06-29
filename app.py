from flask import Flask
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
    response = MessagingResponse()
    response.message('Thanks for texting! Searching for your song now.')

    print("here")
    response = "swag"
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)