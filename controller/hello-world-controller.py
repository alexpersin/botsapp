"""
This controller has an endpoint which SMS messages are forwarded to by Nexmo,
and which replies using the Nexmo client with a default message.

It also has an endpoint for the CLI.

Alex - I'm currently just using this as an test-bed before doing the controller properly.
Some parts (like the config and Message definition) will get moved.
"""

import nexmo
import os
import hug
import pprint


client = nexmo.Client(
    key=os.environ.get("NEXMO_API_KEY"), 
    secret=os.environ.get("NEXMO_API_SECRET")
)


class Message():
    def __init__(self, sender, body, platform):
        self.sender = sender
        self.body = body
        self.platform = platform


@hug.get("/sms")
def handle_sms(msisdn: hug.types.number, to: hug.types.number, text: hug.types.text, **kwargs):
    """ Sends a default reply to anyone who texts BotsApp."""
    for key, val in kwargs.items():
        print(f"{key}: {val}")
    
    client.send_message({
        'from': to,
        'to': msisdn,
        'text': 'Hi from BotsApp!',
    })

    return ('', 200)

@hug.post("/cli")
def handle_cli():


hug.API(__name__).http.serve(port=8000)

print ("Done")
