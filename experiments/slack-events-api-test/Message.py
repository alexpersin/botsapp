
class Message():
    def __init__(self, timestamp, message_sender, message_recipient, message_content):
        self.timestamp         = timestamp
        self.message_content   = message_content
        self.message_sender    = message_sender
        self.message_recipient = message_recipient

    def __str__(self):
        return '''Message:
        From: %s
        Content: %s ''' % (self.message_sender, self.message_content)
    
    def __repr__(self):
        return 'Message(From: %s, Content: %s)' % (self.message_sender, self.message_content)
    