# Import reduce from functool
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2 , stark)

# Print the result
print(result)

#The call len(525600) raises a TypeError.