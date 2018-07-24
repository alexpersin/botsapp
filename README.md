Botsapp
=======

A chatbot

# Notes
- Yowsup is really dead now with the version of whatsapp it used being completely deprecated.
- Trying to setup WhatsappWebWrapper and a version of the Whatsapp app running in Chrome using ARC and inside a docker container - see experiments/chrome-in-docker.

### Platform Integrations
Most messaging services use have a HTTP API you can send messages to, then you register a webhook with them that links to an end point on your web server and then messages sent to you are sent to you via a POST request to that end point. Hence the bot should consist of a web server with handlers respond to the incoming messages.
- We could support SMS and voice calls using Nexmo or alternative.
- Would also support Messenger, Slack, Mattermost etc, which all provide HTTP APIs with webhooks.

### Bot libraries
Botkit looks like the best option for a controller... if we wanted to write Javascript. There doesn't look like any good alternatives in Python, but maybe we want to write it ourselves anyway.

### Deployment
Possible options:
- Deploy as Docker containers onto a VPS or onto a cloud container hosting service
- Deploy services individually onto a VPS