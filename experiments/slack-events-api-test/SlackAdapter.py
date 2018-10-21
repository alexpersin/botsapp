from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os
from Message import Message

'''Basic slack adapater class. On init it expects you to have defined the SLACK_SIGNING_SECRET and SLACK_BOT_TOKEN.
   I will show you where to find these'''

class SlackAdapter():

    def send_message(self, channel, message):
        self.slack_client.api_call("chat.postMessage", channel=channel, text=message)

    def _slack_message_conversion(self, message):
        botsapp_message = Message(message["event_ts"])
        botsapp_message.set_message_content(message["user"], "", message["text"])
        return botsapp_message

    
    
    def __init__(self):
        self.slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
        self.slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
        
        self.slack_events_adapter = SlackEventAdapter(self.slack_signing_secret, "/slack/events")
        self.slack_client = SlackClient(self.slack_bot_token)

        '''Not sure how else to do this because of the @, Alex maybe you can explain what is going on but it seems
           I have to have this block of code here and not as a separate method. I've just set it to print out the
           message for now, I guess it is in here we can make it do whatever we want.'''

        @self.slack_events_adapter.on("message")
        def handle_message(event_data):
            message = event_data["event"]
            output_message = self._slack_message_conversion(message)
            output_message.print_message()
        
        self.slack_events_adapter.start(port=3000)
        






        
