#pip install requests
import re
import pandas as pd
import requests
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


# Make a sample HTTP request
url = 'https://app.e-builder.net/da2/Documents/FileView.aspx?FileID=f3f9f221-dff5-4d66-9667-ba820f6132e3'
response = requests.get(url)

# Check the content-type header
content_type = response.headers.get('content-type', '')

# Check if the content-type indicates a PDF or if the response content starts with '%PDF'
is_pdf = content_type.lower().startswith('application/pdf') or response.content.startswith(b'%PDF')

if is_pdf:
    print(f'The URL {url} seems to point to a PDF file.')
else:
    print(f'The URL {url} does not appear to be a PDF file.')