from prompt_toolkit import prompt
from aiohttp import web
import asyncio
import requests
import sys


BOT_URL = "localhost:8000" # the default value can be overriden as a CL arg when running this program

# the CLI redefines the Message class because its message format
# doesn't *have* to be the same as the controller (c.f. slack's
# message format is different). Redefining it here means that
# changes to its format don't have to be compatible with the 
# controller
class Message():
    def __init__(self, sender, body, platform):
        self.sender = sender
        self.body = body
        self.platform = platform    


async def prompt_loop():
    while True:
        user_input = prompt(f'{username}:')
        print(user_input)
        requests.post()
        await asyncio.sleep(0.01)


async def handle_incoming_message(request):
    sender = request.match_info.get('sender', "Anonymous")
    body = request.match_info.get('body', "")
    print(f"{sender}: {body}")

    return web.Response(body=None, status=200)


def run():
    app = web.Application()
    app.add_routes([web.get('/', handle_incoming_message)])
    asyncio.ensure_future(prompt_loop())
    web.run_app(app)


def main():
    if len(sys.argv) > 1:
        BOT_URL = sys.argv[1]

    print("--- Botsapp Command Line Interface ---\n")
    global username
    username = prompt('Enter your name:')
    run()


if __name__ == "__main__":
    main()
