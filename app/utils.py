import logging


def config_logging():
    """
    Config logging
    """
    format = "[%(filename)s:%(lineno)s - %(funcName)s ] %(message)s"
    # log to file
    # logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename=os.path.join(os.getcwd(), "log.log"))
    # log to stdout
    logging.basicConfig(format=format, level=logging.DEBUG)
