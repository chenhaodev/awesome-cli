#pip install googlesearch-python
from googlesearch import search
import os, sys

# Query to search
query = sys.argv[1] #"skin cancer"

# Perform the Google search in En and Zh
search_results = search(query, num_results=12, lang='en', advanced=True)
print('======En info======')
for i, result in enumerate(search_results, start=1):
    print(f"Result {i}: {result}")

search_results = search(query, num_results=8, lang='zh', advanced=True)
print('======Zh info======')
for i, result in enumerate(search_results, start=1):
    print(f"Result {i}: {result}")
