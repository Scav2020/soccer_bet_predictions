import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Read csv files
overall_data = pd.read_csv('overall.csv')
home_data = pd.read_csv('home.csv')
away_data = pd.read_csv('away.csv')

# Combine dataframes
frames = [overall_data, home_data, away_data]
all_data = pd.concat(frames)

def main():
    # Calculate correlation matrix
    corr_matrix = all_data.corr()

    # Visualize correlation matrix using heatmap
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

    # Print significant correlations
    threshold = 0.5
    significant_corrs = np.where(np.abs(corr_matrix) > threshold)
    print('Significant Correlations:')
    for i in range(len(significant_corrs[0])):
        feature1 = corr_matrix.columns[significant_corrs[0][i]]
        feature2 = corr_matrix.index[significant_corrs[1][i]]
        corr_val = corr_matrix.iloc[significant_corrs[0][i], significant_corrs[1][i]]
        print(f'{feature1} vs {feature2}: {corr_val}')

    # Plot scatter plots for significant correlations
    for i in range(len(significant_corrs[0])):
        feature1 = corr_matrix.columns[significant_corrs[0][i]]
        feature2 = corr_matrix.index[significant_corrs[1][i]]
        sns.scatterplot(data=all_data, x=feature1, y=feature2)


if __name__ == '__main__':
    main()