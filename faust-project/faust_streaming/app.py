import logging

import faust
from mode import get_logger

from simple_settings import settings
from logging.config import dictConfig


app = faust.App(
    autodiscover=True,
    origin='faust_streaming',
    broker=settings.KAFKA_BOOTSTRAP_SERVER,
    id="1",
)




def main() -> None:
    app.main()


if __name__ == '__main__':
    main()
