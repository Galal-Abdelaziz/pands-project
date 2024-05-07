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
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'] # Columns headers of the data DataFrame, to make it easier to work with the dataset.

## Save a summary of each variable to a text file.
with open('summary.txt', 'w') as f:     
    f.write('Summary of each variable:\n\n')    # Write a header to the file.
    f.write(data.describe().to_string())        # Write the summary statistics to the file.

## Save a histogram of each variable to a png file.
fig, axes = plt.subplots(2, 2, figsize=(10,10))  # Create a 2x2 grid of subplots.
axes[0,0].hist(data['sepal_length'], bins=7)  # Create a histogram of sepal length.
axes[0,0].set_title('Sepal Length')  # Set the title of the subplot.
axes[0,1].hist(data['sepal_width'], bins=5)  # Create a histogram of sepal width.
axes[0,1].set_title('Sepal Width')  # Set the title of the subplot.
axes[1,0].hist(data['petal_length'], bins=6)  # Create a histogram of petal length.
axes[1,0].set_title('Petal Length')  # Set the title of the subplot.
axes[1,1].hist(data['petal_width'], bins=6)  # Create a histogram of petal width.
axes[1,1].set_title('Petal Width')  # Set the title of the subplot.
plt.savefig('histograms.png')  # Save the plot to a png file.

## Set the seaborn style and create a pairplot of each pair of variables.
sns.set(rc={'figure.figsize':(10,10), 'figure.autolayout': True})
#sns.pairplot(data.drop('species', axis=1), diag_kind='hist')  # Create a pairplot of each pair of variables, excluding the 'species' column.
sns.pairplot(data, hue='species', diag_kind='hist')  # Create a pairplot of each pair of variables, excluding the species, with different colors for each species.
plt.savefig('scatter_plots.png')  # Save the plot to a png file.

## Perform extra analysis plotting them and saving to the other_analysis txt file.
# Calculate the correlation matrix.
corr_matrix = data.drop('species', axis=1).corr()

# Calculate the mean and standard deviation of each variable for each species.
grouped = data.groupby('species').describe()

# Plot the correlation matrix as a heatmap.
plt.figure(figsize=(10, 10))  # Create a new figure with a size of 10x10 inches.
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)  # Use seaborn's heatmap function to plot the correlation matrix.
plt.title('Correlation Matrix')  # Set the title of the plot.
plt.savefig('correlation_matrix.png')  # Save the plot to a file named 'correlation_matrix.png'.

# Plot the mean and standard deviation of each variable for each species as scatter plots.
plt.figure(figsize=(10, 10))  # Create a new figure with a size of 10x10 inches.
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=data)  # Use seaborn's scatterplot function to plot sepal length vs sepal width.
plt.title('Sepal Length vs Sepal Width')  # Set the title of the plot.
plt.savefig('sepal_length_vs_sepal_width.png')  # Save the plot to a file named 'sepal_length_vs_sepal_width.png'.

plt.figure(figsize=(10, 10))  # Create a new figure with a size of 10x10 inches.
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=data)  # Use seaborn's scatterplot function to plot petal length vs petal width.
plt.title('Petal Length vs Petal Width')  # Set the title of the plot.
plt.savefig('petal_length_vs_petal_width.png')  # Save the plot to a file named 'petal_length_vs_petal_width.png'.

# Plot the number of samples of each species as a pie chart
plt.figure(figsize=(8, 8))  # Create a new figure with a size of 8x8 inches
plt.pie(data['species'].value_counts(), labels=data['species'].unique(), autopct='%1.1f%%')  # Use matplotlib's pie function to plot the number of samples of each species.
plt.title('Number of Samples of Each Variety')  # Set the title of the plot.
plt.savefig('number_of_samples.png')  # Save the plot to a file named 'number_of_samples.png'.

# Save the correlation matrix, mean and standard deviation, and number of samples of each species to a text file.
with open('other_analysis.txt', 'w') as f:
    f.write('Correlation matrix:\n\n') # Write the correlation matrix to the file.
    f.write(corr_matrix.to_string())
    f.write('\n\nMean and standard deviation of each variable for each species:\n\n')  # Write the mean and standard deviation of each variable for each species to the file.
    f.write(grouped.to_string())
    f.write('\n\nNumber of samples of each species:\n\n') # Write the number of samples of each species to the file.
    f.write(data['species'].value_counts().to_string())