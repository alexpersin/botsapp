from core import Message

class SlackMessage(Message):
    def __init__(self,  sender, body, recipient=None, timestamp=None):
        super(SlackMessage, self).__init__(sender, bost, recipient, timestamp, platform="slack")
