from core import Message

class Adapter(object):
    """ Base class for all adapters. """
    def __init__(self):
        pass

    def send(self, message: Message):
        """ This will be called by botsapp. It should add any adapter specific
        information to the argument message object then send it. """
        raise NotImplementedError()

    def add_handler(self, handler):
        """ When a message is received, the subclass should call this
            handler with the message as its argument """
        raise NotImplementedError()

    def run(self):
        """ Starts the adapter """
        raise NotImplementedError()
