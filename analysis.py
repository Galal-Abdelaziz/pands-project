# analysis.py
# Project for Programming and Scripting.
# Fisher’s Iris data set analysis.
# A program that does the following: Outputs a summary of each variable to a single text file; Saves a histogram of each variable to png files; Outputs a scatter plot of each pair of variables; Performs other appropriate analysis.
# Author: Galal Abdelaziz

import pandas as pd  # Import the pandas library for data manipulation.
import seaborn as sns  # Import the seaborn library for visualization.
import matplotlib.pyplot as plt  # Import the matplotlib library for visualization.
import warnings  # Import the warnings library to suppress a warning message.

warnings.filterwarnings("ignore", category=UserWarning)  # Ignore UserWarning messages.

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv') # Load the Iris data set from the given URL.
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']     # Columns headers of the data DataFrame, to make it easier to work with the dataset.

## Define a color palette
palette = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}                      # Define colors for each species using dictionary.

## Save a histogram (colors for each species) of each variable to a png file.
fig, axes = plt.subplots(2, 2, figsize=(10,10))               # Create a 2x2 grid of subplots.
for ax, column in zip(axes.flatten(), data.columns[:-1]):     # Iterate over each feature (column) in data DataFrame.
    for species, group in data.groupby('species'):            # Iterate over each species in data DataFrame.
        ax.hist(group[column], bins=7, alpha=0.5, label=species, color=palette[species]) # Create histogram for species with specified color.
    ax.set_title(column.capitalize())                         # Set title of histogram with capitalized column name.
    ax.legend()                                               # Add legend.
plt.tight_layout()                                            # Ensure subplots don't overlap.
plt.savefig('variable_histograms.png')                        # Save the plot to a file named 'variable_histograms.png'.

## Set the seaborn style and create a pairplot of each pair of variables.
sns.set(rc={'figure.figsize':(10,10), 'figure.autolayout': True})    # Set seaborn style.
sns.pairplot(data, hue='species', diag_kind='hist', palette=palette) # Create pairplot of each pair of variables with different colors for each species.
plt.savefig('variable_scatterplots.png')                             # Save the plot to a file named 'variable_scatterplots.png'.

## Perform extra analysis plotting them and saving to the other_analysis txt file.
# Calculate the correlation matrix.
corr_matrix = data.drop('species', axis=1).corr() 

# Calculate the mean and standard deviation of each variable for each species.
grouped = data.groupby('species').describe()      

# Plot the correlation matrix as a heatmap.
plt.figure(figsize=(10, 10))                                    # Create a new figure with a size of 10x10 inches.
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True) # Use seaborn's heatmap function to plot the correlation matrix.
plt.title('Correlation Matrix')                                 # Set the title of the plot.
plt.savefig('variable_correlation_matrix.png')                  # Save the plot to a file named 'correlation_matrix.png'.

# Plot the mean and standard deviation of each variable for each species as scatter plots.
plt.figure(figsize=(10, 10))                                    # Create a new figure with a size of 10x10 inches.           
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=data, palette=palette) # Use seaborn's scatterplot function to plot sepal length vs sepal width.
plt.title('Sepal Length vs Sepal Width')                        # Set the title of the plot.
plt.savefig('sepal_length_vs_sepal_width.png')                  # Save the plot to a file named 'sepal_length_vs_sepal_width.png'.

plt.figure(figsize=(10, 10))                                    # Create a new figure with a size of 10x10 inches.
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=data, palette=palette) # Use seaborn's scatterplot function to plot petal length vs petal width.
plt.title('Petal Length vs Petal Width')                        # Set the title of the plot.
plt.savefig('petal_length_vs_petal_width.png')                  # Save the plot to a file named 'petal_length_vs_petal_width.png'.

# Plot the number of samples of each species as a pie chart
plt.figure(figsize=(8, 8))                                      # Create a new figure with a size of 8x8 inches.
plt.pie(data['species'].value_counts(), labels=data['species'].unique(), autopct='%1.1f%%', colors=[palette[s] for s in data['species'].unique()])  # Use matplotlib's pie function to plot the number of samples of each species.
plt.title('Number of Samples of Each Species')                   # Set the title of the plot.
plt.savefig('number_of_samples.png')                             # Save the plot to a file named 'number_of_samples.png'.

## Save a summary of each variable (combined and separate) to a text file.
with open('variable_summary.txt', 'w') as f:                  # Generates a file named 'variable_summary.txt' on write mode.
    f.write('**** Iris Data Set Analysis ****\n\n')           # Write a header to the file.
    f.write('Overall Summary:\n\n')                           # Write a header to the file.
    f.write(data.describe().to_string())                      # Write the summary statistics to the file.
    f.write('\n\nSummary Of Each Variable:\n\n')              # Write a header to the file.
    for column in data.columns[:-1]:                          # Iterate over each feature (column) in data DataFrame.
        f.write('Variable: {}\n'.format(column))                         # Write the name of the variable to the file.
        f.write('Minimum value: {}\n'.format(data[column].min()))        # Write the minimum value of the variable to the file.
        f.write('Maximum value: {}\n'.format(data[column].max()))        # Write the maximum value of the variable to the file.
        f.write('Mean value: {}\n'.format(data[column].mean()))          # Write the mean value of the variable to the file.
        f.write('Standard deviation: {}\n\n'.format(data[column].std())) # Write the standard deviation value of the variable to the file.
    f.write('**** Extra Analysis ****\n\n')                          # Write a header to the file.
    f.write('Correlation matrix:\n\n')                                   # Write a header to the file.
    f.write(corr_matrix.to_string())                                     # Write the correlation matrix to the file.
    f.write('\n\nNumber of samples of each species:\n\n')                # Write a header to the file.
    f.write(data['species'].value_counts().to_string())                  # Write the Number of samples of each species to the file.