

import faust


app = faust.App(
    autodiscover=True,
    origin='faustapp',
    id='django-proj',
)


import os

# make sure the event loop is used as early as possible.
os.environ.setdefault('FAUST_LOOP', 'eventlet')

# set the default Django settings module for the 'faust' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


@app.on_configured.connect
def configure_from_settings(app, conf, **kwargs):
    from django.conf import settings
    conf.broker = settings.KAFKA_BOOTSTRAP_SERVER

def main() -> None:
    app.main()


if __name__ == '__main__':
    main()
