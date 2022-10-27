from faustapp.records import Greeting
from faustapp.app import app

topic = app.topic('hello-topic', value_type=Greeting)


