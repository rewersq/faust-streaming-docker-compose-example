import logging

from faust_streaming.app import app
from mode import get_logger
from faust_streaming.topics import topic

logging_logger = logging.getLogger(__name__)
mode_logger = get_logger(__name__)
@app.agent(topic)
async def hello(greetings):
    async for greeting in greetings:
        logging_logger.info(f'logging Hello from {greeting.from_name} to {greeting.to_name}')
        logging_logger.warning(f'logging Hello from {greeting.from_name} to {greeting.to_name}')
        logging_logger.error(f'logging Hello from {greeting.from_name} to {greeting.to_name}')
        mode_logger.info(f'mode_logger Hello from {greeting.from_name} to {greeting.to_name}')
        mode_logger.warning(f'mode_logger Hello from {greeting.from_name} to {greeting.to_name}')
        mode_logger.error(f'mode_logger Hello from {greeting.from_name} to {greeting.to_name}')
        print(f'print Hello from {greeting.from_name} to {greeting.to_name}')
