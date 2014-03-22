# Pubsub HTTP streaming proof-of-concept

This is a basic pubsub HTTP streaming server, using redis as the pubsub broker, flask as a lightweight web framework, and gevent for high concurrency non-blocking I/O.

Here's how to run it:

1. Start up a local redis server.
2. Create a virtualenv for the project and run `pip install -r requirements.txt`.
3. Run `python publish.py` to start publishing messages to the pubsub channel.
4. Run `python server.py` to start a gevent-based web server listening for requests on `http://127.0.0.1:5000/stream/<id>` where `<id>` is any integer.
5. Run `python subscribe.py` to spawn greenlets to read messages from the pubsub channel.
