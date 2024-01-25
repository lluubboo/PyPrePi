import pandas
from sklearn.model_selection import train_test_split
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

logger.info("Correlation matrix (Pearsons):")
logger.info(data_frame.corr())

logger.info("Correlation matrix (Kendall):")
logger.info(data_frame.corr(method='kendall'))

logger.info("Correlation matrix (Spearman):")
logger.info(data_frame.corr(method='spearman'))

test_size = 0.2
train_data_frame, test_data_frame = train_test_split(data_frame, test_size, random_state=123456, shuffle=True, stratify=data_frame['target'])
logger.info("Data frame split into training and test set with test size " + str(test_size))

# Save the data frames to CSV file as output for the next step
merged_data_frame = pandas.concat([train_data_frame, test_data_frame])
merged_data_frame.to_csv('output/merged_data.csv', index=False)
logger.info("Merged data frame saved to output folder.")