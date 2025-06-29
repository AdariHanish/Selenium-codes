import logging

def get_logger(name='AutomationLogger'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Set up file handler to write logs to a file
    fh = logging.FileHandler('reports/framework.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
