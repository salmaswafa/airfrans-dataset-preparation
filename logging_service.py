import logging

def setup_logging():
    # console
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

    # file
    # logging.basicConfig(filename='app.log', level=logging.INFO,
    #                     format='%(asctime)s - %(levelname)s - %(message)s')
    