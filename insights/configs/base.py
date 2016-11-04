""" Configuration class for Insights"""

import logging
import os

from logging import config

LOGGER = logging.getLogger(__name__)

def get_project_root():
    """Return the path to the Insights project root directory.
    :return: A directory path.
    :rtype: str
    """
    return os.path.realpath(os.path.join(
         os.path.dirname(__file__),
         os.pardir,
         os.pardir,
    ))

class Settings(object):
    """
    Insights Settings representation.
    """

    def __init__(self):
        """
        Init for Settings
        """
        self._configured = False

    def configure(self):
        self._configure_logging()
        self._configured = True

    def _configure_logging(self):
        """Configure logging for Insights.

        It will load configuration from logging.conf if present
        in root directory, otherwise custom logging format is used by
        default

        """

        if self.configured:
            LOGGER.info("Already configured")
            return

        # All output should be made by the logging module, including warnings
        logging.captureWarnings(True)

        # Allow overriding logging config based on the presence of logging.conf
        # file on Insights's project root
        logging_conf_path = os.path.join(get_project_root(), 'logging.conf')
        if os.path.isfile(logging_conf_path):
            config.fileConfig(logging_conf_path)
        else:
            logging.basicConfig(
                format='%(levelname)s %(module)s:%(lineno)d: %(message)s'
            )

    @property
    def configured(self):
        """Returns True if the settings have already been configured."""
        return self._configured
