from faustapp.app import app
from faustapp.records import Greeting
from faustapp.agents import hello


@app.timer(interval=1.0)
async def example_sender(app):
    await hello.send(
        value=Greeting(from_name='Faust', to_name='you'),
    )