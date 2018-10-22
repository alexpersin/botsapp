from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
from get_functions import *
import os
import re

VERBOSE = True

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = SlackClient(slack_bot_token)




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
        slack_client.api_call("chat.postMessage", channel=channel, text=message)


# Echo any slack reaction
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.api_call("chat.postMessage", channel=channel, text=text)


@slack_events_adapter.on("message")
def call_everyone_a_cunt(event_data):
    message = get_message(event_data)
    channel = get_channel(message)
    if bot_mentioned(event_data):
        slack_client.api_call("chat.postMessage", channel=channel, text="You are all cunts")
# C@hecks if the bot has been mentioned in chat
def bot_mentioned(event_data):
    message = event_data["event"]
    channel = message["channel"]
    if message.get("subtype") is None and get_user_id(slack_client) in message.get("text"):
        slack_client.api_call("chat.postMessage", channel=channel, text="Stop talking about me.")
        return True

# Listens to chat for a given phrase
def listen_for_phrase(event_data, phrase):
    message = get_message(event_data)
    channel = get_channel(message)
    if message.get("subtype") is None and phrase in message.get("text"):
        return True

# Configure to port of Flask server or I am using ngrok

slack_events_adapter.start(port=3000)