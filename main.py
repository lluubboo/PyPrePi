import pandas
import logging
import io_utilities 
import plot_utilities

# Set up logging
logger = io_utilities.init_logger()

logger.info("Data preprocessing pipeline started...")

file = io_utilities.select_file()

logger.info("File selected: " + file)

data_frame = pandas.read_csv(file, sep=io_utilities.guess_delimiter(file))

logger.info("Data frame created.")

logger.info(data_frame.describe())

plot_utilities.plot_histograms(data_frame)

logger.info("Histograms exported.")

logger.info("Correlation matrix:")
logger.info(data_frame.corr())