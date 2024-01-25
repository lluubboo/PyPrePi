import tkinter 
import logging
from tkinter import filedialog

def select_file():
    """
    Opens a file selection dialog and returns the selected file path.

    Returns:
        str: The selected file path.
    """
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def init_logger():
    """
    Initializes and configures a logger for data preprocessing.

    Returns:
        logger (logging.Logger): The configured logger object.
    """
    
    # Set up logging
    logger = logging.getLogger('DATA PREPROCESSING')
    logger.setLevel(logging.INFO)

    # Create a file handler
    handler = logging.FileHandler('data_preprocessing.log')
    handler.setLevel(logging.INFO)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a logging format
    formatter = logging.Formatter('%(name)s - %(levelname)s \n%(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)

    return logger

def guess_delimiter(file):
    """
    Guesses the delimiter used in a file based on the first line.

    Args:
        file (str): The path to the file.

    Returns:
        str: The guessed delimiter. If no delimiter is found, ',' (comma) is returned as the default.

    """
    with open(file, 'r') as f:
        first_line = f.readline()
    for delimiter in [',', '\t', ';', '|']:
        if delimiter in first_line:
            return delimiter
    return ','  # Default to comma