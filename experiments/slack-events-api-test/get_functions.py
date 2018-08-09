
def get_user_id(slack_bot_client):
    user_id = slack_bot_client.api_call("auth.test")["user_id"]
    return user_id

def get_message(event_data):
    message = event_data["event"]
    return message

def get_channel(message):
    channel = message["channel"]
    return channel

def get_sender_user(message):
    user = message["user"]
    return user