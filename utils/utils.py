import logging


def get_logger(name, level=logging.INFO, format='%(asctime)s [%(name)s] [%(levelname)s] %(message)s'):
    logging.basicConfig(format=format)
    logger = logging.getLogger(name=name)
    logger.setLevel(level)
    return logger