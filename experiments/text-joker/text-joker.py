"""
This mini app allows the user to send a text that appears to come from someone 
else.
"""

import nexmo
import os
import re
import hug
import pprint


class UserError(Exception):
    """ An error whose message will be sent to the user. """
    pass


client = nexmo.Client(
    key=os.environ.get("NEXMO_API_KEY"), 
    secret=os.environ.get("NEXMO_API_SECRET")
)


with open("allowed_phone_numbers.txt", "r") as f:
    allowed_nums = {int(line.split(" ", 1)[1]) for line in f.readlines()}


def handle_user_errors(f):
    """ Catches UserErrors and sends them to the user """
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except UserError as e:
            print(e)
            client.send_message({
                'from': os.environ.get("NEXMO_PHONE_NUM"),
                'to': kwargs["msisdn"],
                'text': str(e),
            })
            client.send_message({
                'from': os.environ.get("NEXMO_PHONE_NUM"),
                'to': os.environ.get("ALEX_PHONE_NUM"),
                'text': str(e),
            })
            return ('', 200)           

    return wrapped


@hug.get("/sms")
@handle_user_errors
def sms(msisdn: hug.types.number, to: hug.types.number, text: hug.types.text, **kwargs):
    """ Looks for messages in the format <phone num> <from name> <message body>"""
    for key, val in kwargs.items():
        print(f"{key}: {val}")

    if int(msisdn) not in allowed_nums:
        print("Phone number not allowed.")
        return ('', 200)
    
    try:
        to_num, from_name, message = text.split(" ", 2)
    except ValueError:
        raise UserError("The message needs to be: "
            "<number> <from> <message> where the number is a UK mobile number"
            "and the <from> is up to 9 letters no spaces.")
        
    to_num = _parse_number(to_num)
    from_name = _parse_from_name(from_name)

    if(len(message) > 480):
        raise UserError(f"The message is too long ({len(message)}/480 characters)")

    client.send_message({
        'from': from_name,
        'to': to_num,
        'text': message,
    })
    client.send_message({
        'from': from_name,
        'to': os.environ.get("ALEX_PHONE_NUM"),
        'text': message,
    })

    return ('', 200)


def _parse_number(to_num):
    m = re.match(r"^\d+$", to_num)
    if not (m):
        raise UserError(
            f"The first word '{to_num[:30]}' needs to be a UK phone number."
        )
    else:
        m = m.group(0)

    if m.startswith("0044"):
        m = m[2:]
    elif m.startswith("+44"):
        m = m[1:]
    elif m.startswith("07"):
        m = "44" + m[1:]
    if len(m) != 12:
        raise UserError(
            f"The first word '{to_num[:30]}' needs to be a UK phone number."
        )

    return int(m)


def _parse_from_name(from_name):
    m = re.match(r"^\w{1,9}$", from_name)
    if not (m):
        raise UserError(
            f"The second word '{from_name[:30]}' needs to be a a word of up to 9 letters."
        )

    return m.group(0)
    

hug.API(__name__).http.serve(port=8000)
