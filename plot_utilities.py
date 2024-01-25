import matplotlib.pyplot as plt

def plot_histograms(data_frame):
  # Create a histogram for each column
    for column in data_frame:
        plt.figure()  # Create a new figure
        data_frame[column].hist(bins=50)  # Create a histogram
        plt.title(column)  # Set the title of the histogram
        plt.savefig(f'histograms/{column}.png')  # Save the histogram to a file