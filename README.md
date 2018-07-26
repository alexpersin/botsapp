Botsapp
=======

A chatbot

## Architecture
There are three main components. 

#### Messaging platform integrations
If the platform already provides an HTTP API we don't have to do anything. If they don't we need to build an HTTP API ourselves around whatever they do have.

#### Bot Controller
This is the main part of the bot. It has is both a web server and client to send and receive messages. It converts the messages from their platform specific form into a generic form and passes them to a layer which decides what to do with the message. 

#### Plugins
If the message requests an action to be performed (like play a song on Spotify), there should be a framework for connecting plugins to the controller to perform these requests. This will allow the code to be separate and will offload work away from the controller.

## Notes
- Yowsup is really dead now with the version of whatsapp it used being completely deprecated.
- Trying to setup WhatsappWebWrapper and a version of the Whatsapp app running in Chrome using ARC and inside a docker container - see experiments/chrome-in-docker.
- Many web microframeworks are available, Hug looks best for synchronous programming and aiohttp for asynchronous.

## Platform Integrations
Most messaging services use have a HTTP API you can send messages to, then you register a webhook with them that links to an end point on your web server and then messages sent to you are sent to you via a POST request to that end point. Hence the bot should consist of a web server with handlers respond to the incoming messages.
- We could support SMS and voice calls using Nexmo or alternative.
- Would also support Messenger, Slack, Mattermost etc, which all provide HTTP APIs with webhooks.
- It might be possible to support Messenger without talking to a facebook Page (e.g. in a group chat) by building a bot

## Bot libraries
Botkit looks like a great bot framework but it's in Javascript and we probably want to write it ourselves anyway. There doesn't look like there are any good existing alternatives in Python.

## Deployment
Possible options:
- Deploy as Docker containers onto a VPS or onto a cloud container hosting service
- Deploy services individually onto a VPS