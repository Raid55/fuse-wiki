from api.app import app as application
from raven import Client
import logging
# from raven.middleware import Sentry
from os import getenv

# application = Sentry(
    # app,
    # Client(getenv('SENTRY_DSN'))
# )

if __name__ == "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    application.logger.handlers = gunicorn_logger.handlers
    application.logger.setLevel(gunicorn_logger.level)
    application.run()
