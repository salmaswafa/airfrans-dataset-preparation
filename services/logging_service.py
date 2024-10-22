import logging

def setup_logging(console_level: int = logging.DEBUG, 
                  file_level: int = logging.INFO, 
                  log_to_file: bool = False, 
                  filename: str = 'app.log') -> None:
    """Set up logging configuration for the application.

    Args:
        console_level (int): The logging level for console output (default is DEBUG).
        file_level (int): The logging level for file output (default is INFO).
        log_to_file (bool): Whether to log messages to a file (default is False).
        filename (str): The filename for the log file if logging to file is enabled (default is 'app.log').
    """
    # Setup console logging
    logging.basicConfig(level=console_level,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Suppress verbose logs from matplotlib
    logging.getLogger('matplotlib').setLevel(logging.WARNING)

    if log_to_file:
        # Setup file logging if enabled
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(file_level)
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        
        # Add the file handler to the root logger
        logging.getLogger().addHandler(file_handler)