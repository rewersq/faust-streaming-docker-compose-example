from faust_streaming.app import app
from faust_streaming.records import Greeting
from faust_streaming.agents import hello


@app.timer(interval=1.0)
async def example_sender(app):
    await hello.send(
        value=Greeting(from_name='Faust', to_name='you'),
    )