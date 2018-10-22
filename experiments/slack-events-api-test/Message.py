
class Message():
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.message_content = ''
        self.message_sender  = ''
        self.message_recipient = ''

    def set_message_content(self, message_sender, message_recipient, message_content):
        self.message_content = message_content
        self.message_sender  = message_sender
        self.message_recipient = message_recipient

    def print_message(self):
        print('''Message:\n \
                 From: %s\n \
                 Content %s''' % (self.message_sender, self.message_content))