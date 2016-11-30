import logging

LOGGER = logging.getLogger('insights')
LINECOUNT = 50


class Util:

    @staticmethod
    def print_testname(cls, method):
        LOGGER.info("\n")
        LOGGER.info("-" * LINECOUNT)
        LOGGER.info("{0}:{1}".format(cls, method.__name__))
        LOGGER.info("-" * LINECOUNT)

    @staticmethod
    def log_assert(test, msg):
        """
        If assertion is False, log the message in
        logger error
        """
        if not test:
            LOGGER.error(msg)
            assert test, msg
