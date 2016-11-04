import logging

LOGGER = logging.getLogger('insights_api')
LINECOUNT = 50

class Util:

    @staticmethod
    def print_testname(cls, method):
        LOGGER.info("\n")
        LOGGER.info("-" * LINECOUNT)
        LOGGER.info("{0}:{1}".format(cls, method.__name__))
        LOGGER.info("-" * LINECOUNT)