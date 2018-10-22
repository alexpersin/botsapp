import os
from slackclient import SlackClient
from slackeventsapi import SlackEventAdapter

from adapters import Adapter
from adapters.slack.message import SlackMessage

class SlackAdapter(Adapter):
    '''Basic slack adapater class. On init it expects you to have defined the SLACK_SIGNING_SECRET and SLACK_BOT_TOKEN.
       I will show you where to find these.'''
    def __init__(self, port=3000):
        self.signing_secret = os.environ["SLACK_SIGNING_SECRET"]
        self.bot_token = os.environ["SLACK_BOT_TOKEN"]

        self.events_adapter = SlackEventAdapter(self.signing_secret, "/slack/events")
        self.client = SlackClient(self.bot_token)
        self.port = port
        self.adapater_running = False
        self.handler = None

    def send_message(self, channel, message):
        self.slack_client.api_call("chat.postMessage", channel=channel, text=message)

    def get_display_name(self, user_id):
        # TODO cache these results, raise an error don't return
        users_list = self.client.api_call("users.list")
        if users_list["ok"]:
            members = users_list["members"]
            for member in members:
                if member["id"] == user_id:
                    return member["profile"]["display_name"]
            return "Could not find user id %" % user_id
        else:
            return "Could not get users list"

    def _message_conversion(self, message):
        botsapp_message = SlackMessage(message["event_ts"], self.get_display_name(message["user"]), "", message["text"])
        return botsapp_message

    def add_handler(self, handler):
        @self.events_adapter.on("message")
        def handle_message(event_data):
            message = event_data["event"]
            output_message = self._message_conversion(message)
            handler(output_message)

    def __str__(self):
        return "SlackAdapter(port: %i )" % (self.port)

    def __repr__(self):
        return "SlackAdapter(port: %i )" % (self.port)

    def run(self, port=3000):
        self.port = port
        self.events_adapter.start(port=port)
