import pandas as pd

# Example for a comma-delimited .data file
df = pd.read_csv("ji.csv")


# Example for a tab-delimited .data file
# df = pd.read_csv(file_path, sep='\t')

# Example for a whitespace-delimited .data file
# df = pd.read_table(file_path, sep='\s+')

# Print the first few rows to verify
df.head()
df.info()
df.describe()
