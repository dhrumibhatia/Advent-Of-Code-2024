# Day 1: Historian Hysteria

# def main():

import pandas as pd

# Load the file
file_path = '1input.txt'

# Read the file into a dataframe
df = pd.read_csv(file_path, sep='\s+', header=None)
print(df)

