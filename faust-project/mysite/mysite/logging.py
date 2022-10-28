from logging import Handler


class LoggingModelHandler(Handler):
    def __init__(self, field_name):
        super().__init__()
        self.field_name = field_name

    def emit(self, record):
        obj = getattr(record, self.field_name, None)
        if not obj:
            return

        msg = self.format(record)
        obj.add_log(msg)
