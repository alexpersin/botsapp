import datetime
import asyncio

class Message():
    def __init__(self, sender, body, recipient=None, timestamp=None, platform=None):
        self.timestamp = timestamp or datetime.datetime.utcnow()
        self.body = body
        self.sender = sender
        self.recipient = recipient

    def __str__(self):
        return '''Message:
        From: %s
        Content: %s ''' % (self.message_sender, self.message_content)
    
    def __repr__(self):
        return 'Message(From: %s, Content: %s)' % (self.message_sender, self.message_content)


class Bot():
    def __init__(self):
        self.adapters = self.get_adapters()
        self.add_handlers()
    
    def get_adapters(self):
        """ Finds all of the adapters which we have written and instatiates them. """
        # TODO this should look in the adapters directory and automatically
        # fetch all of the adapters. At the moment it's hardcoded to just do slack.
        from adapters.slack.slack_adapter import SlackAdapter
        adapters = [SlackAdapter()]
        return adapters

    def handle(self, message):
        """ This is the method which gets called whenever a message is received 
        on any platform. It should do something with the message. """
        # TODO this is a stub method before an actual handler is implemented
        print(f"Botsapp received a message: {message}")

    def add_handlers(self):
        """ Adds the botsapp message handler to all of the adapters """
        for adapter in self.adapters:
            adapter.add_handler(self.handle)
    
    def run(self):
        """ Runs all the adapters in separate threads. """
        # This is probably not the best way to run all the code asynchronously.
        # I need to brush up on it. (Plus it changed a lot in 3.7)
        print("Starting Botsapp.")
        try:
            loop = asyncio.get_event_loop()
            for adapter in adapters:
                loop.run_until_complete(adapter.run())
            loop.run_forever()
        except KeyboardInterrupt:
            print("Stopping Botsapp.")
        