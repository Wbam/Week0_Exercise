import pandas as pd
from scipy import stats
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import sys


def calculate_summary_statistics(dataframe):
    def is_boolean_column(col):
        unique_values = dataframe[col].dropna().unique()
        return sorted(unique_values) == [0, 1] or sorted(unique_values) == [False, True]

    numerical_columns = dataframe.select_dtypes(include=['float64', 'int64']).columns
    numerical_columns = [col for col in numerical_columns if not is_boolean_column(col)]

    summary_stats = dataframe[numerical_columns].agg(['mean', 'median', 'std']).T
    summary_stats.columns = ['Mean', 'Median', 'Standard Deviation']

    return summary_stats



def count_negative_values(dataframe, columns):
    negative_values = {}
    for column in columns:
        if column in dataframe.columns:
            negative_values[column] = (dataframe[column] < 0).sum()
        else:
            negative_values[column] = None 

    return negative_values



def detect_outliers_zscore(dataframe, columns, threshold=3):

    z_scores = np.abs(stats.zscore(dataframe[columns].dropna()))
    outliers = (z_scores > threshold).sum(axis=0)
    
    return dict(zip(columns, outliers))



def explore_missing_values(dataframe):
    
    missing_values = dataframe.isnull().sum()
    return missing_values


def plot_radiation_data(dataframe, columns, figsize=(14, 10)):
   
    plt.figure(figsize=figsize)
    
    num_plots = len(columns)
    num_rows = (num_plots + 1) // 2
    num_cols = 2 if num_plots > 1 else 1
    
    for i, (col_name, title, y_label, color) in enumerate(columns):
        plt.subplot(num_rows, num_cols, i + 1)
        plt.plot(dataframe.index, dataframe[col_name], label=col_name, color=color)
        plt.title(title)
        plt.xlabel('Time')
        plt.ylabel(y_label)
        plt.legend()
    
    plt.tight_layout()
    plt.show()
