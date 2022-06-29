from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Account SID and Auth Token from www.twilio.com/console
client = Client('ACa3bcc175c3b8fad7e7124c3896064a8c', 'ed79de7746c5046face0c563780b58e8')
app = Flask(__name__)


# A route to respond to SMS messages
@app.route('/sms', methods=['POST', 'GET'])
def inbound_sms():
    response = MessagingResponse()
    response.message('Thanks for texting! Searching for your song now.')

    response = "swag"
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)