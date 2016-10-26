""" Configuration class for Insights"""

import logging
import os

from logging import config

LOGGER = logging.getLogger(__name__)

def get_project_root():
    """Return the path to the Robottelo project root directory.
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
    Insights Settings representattion.
    """

    def __init__(self):
	"""
	Init for Settings
	"""

    def configure(self):
        self._configure_logging()
        self._configured = True

    def _configure_logging(self):
        """Configure logging for Insights.

        It will load configuration from logging.conf if present
        in root directory, otherwise custom logging format is used by
        default

        """

        # All output should be made by the logging module, including warnings
        logging.captureWarnings(True)

        # Set the logging level based on the Insights's verbosity
        #for name in ('insights', 'robotello'):
	#    print "*" * 50
        #    logging.getLogger(name).setLevel(self.verbosity)

        # Allow overriding logging config based on the presence of logging.conf
        # file on Insights's project root
        logging_conf_path = os.path.join(get_project_root(), 'logging.conf')
        if os.path.isfile(logging_conf_path):
            config.fileConfig(logging_conf_path)
        else:
            logging.basicConfig(
                format='%(levelname)s %(module)s:%(lineno)d: %(message)s'
            )
