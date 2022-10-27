from faust_streaming.app import app
from faust_streaming.records import Greeting

topic = app.topic('hello-topic', value_type=Greeting)


