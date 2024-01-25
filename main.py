import pandas
import numpy 
from sklearn.model_selection import train_test_split
import io
import io_utilities 
import plot_utilities

# Set up logging
logger = io_utilities.init_logger()

logger.info("Data preprocessing pipeline started...")

file = io_utilities.select_file()
logger.info("File selected: " + file)

data_frame = pandas.read_csv(file, sep=io_utilities.guess_delimiter(file))
logger.info("Data frame created.")

buffer = io.StringIO()
data_frame.info(buf=buffer)
logger.info(buffer.getvalue())

logger.info(data_frame.describe())

plot_utilities.plot_histograms(data_frame)
logger.info("Histograms exported.")

logger.info("Correlation matrix (Pearsons):")
logger.info(data_frame.corr())

logger.info("Correlation matrix (Kendall):")
logger.info(data_frame.corr(method='kendall'))

logger.info("Correlation matrix (Spearman):")
logger.info(data_frame.corr(method='spearman'))

# prepare reuslting data frame, i want equally distributed values in target column
bins = numpy.linspace(data_frame.iloc[:, -1].min(), data_frame.iloc[:, -1].max()  + 1e-2, 10)
data_frame['efficiency_bins'] = pandas.cut(data_frame.iloc[:, -1], bins, labels=False)
data_frame.to_csv('output/data_with_bins.csv', index=False, sep=';')
bin_counts = data_frame['efficiency_bins'].value_counts()
valid_bins = bin_counts[bin_counts > 1].index
data_frame = data_frame[data_frame['efficiency_bins'].isin(valid_bins)]

test_size = 0.2
data_frame = data_frame.dropna(subset=['efficiency_bins'])
train_data_frame, test_data_frame = train_test_split(data_frame, test_size = test_size, random_state=123456, shuffle=True, stratify=data_frame['efficiency_bins'])
logger.info("Data frame split into training and test set with test size " + str(test_size))

# merge the train and test data frames again because of predefined format
merged_data_frame = pandas.concat([train_data_frame, test_data_frame])

# Remove the 'efficiency_bins' column from the train and test data frames
train_data_frame = train_data_frame.drop(columns=['efficiency_bins'])
test_data_frame = test_data_frame.drop(columns=['efficiency_bins'])

# save the data frames to CSV file as output for the next step
merged_data_frame.to_csv('output/merged_data.csv', index=False, sep=';')
logger.info("Merged data frame saved to output folder.")

buffer = io.StringIO()
merged_data_frame.info(buf=buffer)
logger.info(buffer.getvalue())
logger.info(merged_data_frame.describe())

logger.info("Data preprocessing pipeline finished.")