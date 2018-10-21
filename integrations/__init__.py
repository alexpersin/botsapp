class Platform(object):
    """ Base class for all platform integrations. """
    def __init__(self):
        pass
    
    def send(message: Message):
        """ Adds any platform specific information to the argument message
            object then send it. """
        raise NotImplementedError()

    def add_handler(handler):
        """ When a message is received, the subclass should call this 
            handler with the message as its argument """
        raise NotImplementedError()

