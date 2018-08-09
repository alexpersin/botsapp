from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
from get_functions import *
import os
import re

VERBOSE = False


# Our app's Slack Event Adapter for receiving actions via the Events API
SLACK_VERIFICATION_TOKEN = os.environ["SLACK_VERIFICATION_TOKEN"]
slack_events_adapter = SlackEventAdapter(SLACK_VERIFICATION_TOKEN, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CLIENT = SlackClient(SLACK_BOT_TOKEN)




# Example responder
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    if VERBOSE:
        print(event_data)
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "hi " in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        CLIENT.api_call("chat.postMessage", channel=channel, text=message)


# Echo any slack reaction
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    CLIENT.api_call("chat.postMessage", channel=channel, text=text)



# Checks if the bot has been mentioned in chat
def bot_mentioned(event_data):
    message = event_data["event"]
    channel = message["channel"]
    if message.get("subtype") is None and get_user_id(CLIENT) in message.get("text"):
        CLIENT.api_call("chat.postMessage", channel=channel, text="Stop talking about me.")
        return True

# Listens to chat for a given phrase
def listen_for_phrase(event_data, phrase):
    message = get_message(event_data)
    channel = get_channel(message)
    if message.get("subtype") is None and phrase in message.get("text"):
        return True



# Configure to port of Flask server or I am using ngrok

slack_events_adapter.start(port=3000)