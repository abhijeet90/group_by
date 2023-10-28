import pandas as pd

# Importing cars dataset
cars = pd.read_csv('cars.csv')

# Checking the first 5 rows to get the sense of data
cars.head()

# Creat a group of origin and saved it in a variable origin_group
origin_group = cars.groupby('origin')

# Create a functio find_group which will us the groups in the origin_group variable
def find_group():
    l = []
    for i,j in origin_group:
        l.append(i)
    return l

# Calling function find_group() to check the values
# in this we have three value ['europe', 'japan', 'usa']
find_group()

# Calling a methog get_group which will give us the data associate with the group
# Below code will give us dataframe grouped with europe
origin_group.get_group(find_group()[0])