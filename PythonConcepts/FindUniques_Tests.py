import re
import pandas as pd

# USING re TO CHANGE HOW A TEST SEARCHES FOR A STRING
# Pattern to match 'hyperlink' or 'Hyperlink' (case-insensitive)
pattern = re.compile(r'hyperlink', re.IGNORECASE)

# Test strings
test_string1 = 'hyperlink'
test_string2 = 'Hyperlink'
test_string3 = 'other'

# Test if the strings match the pattern
match1 = pattern.match(test_string1)
match2 = pattern.match(test_string2)
match3 = pattern.match(test_string3)

# Output the results
print(f'Test string 1: {"Match" if match1 else "No match"}')
print(f'Test string 2: {"Match" if match2 else "No match"}')
print(f'Test string 3: {"Match" if match3 else "No match"}')


# CREATING A DATAFRAME WITH TWO COLUMNS
# Sample data
data = {'filepath': ['path1', 'path2', 'path3'],
        'uniques': [set([1, 2, 3]), set(['a', 'b', 'c']), set([10, 20, 30])]}

# Initialize the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)