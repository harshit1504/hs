# Api.ai -webhook implementation in Python

This is a really simple webhook implementation that gets Api.ai classification JSON (i.e. a JSON output of Api.ai /query endpoint) and returns a fulfillment response.

More info about Api.ai webhooks could be found here:
[Api.ai Webhook](https://docs.api.ai/docs/webhook)

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
The services takes the `geo-city` parameter from the action, performs geolocation for the city and requests location of blood bank from Google place API. 

The service packs the result in the Api.ai webhook-compatible response JSON and returns it to Api.ai.
