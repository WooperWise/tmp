import csv
from tmp import *

url_set = set()
no_of_duplicates = 0
with open('links.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    print(f"no of urls found {len(list(reader))}")
    for row in reader:
        url = row[0].strip()
        if url in url_set:
            no_of_duplicates += 1
            print(f"Duplicate URL found: {url}")
        else:
            url_set.add(url)
print(f"No of duplicates found {no_of_duplicates}")
print("Duplicate check complete!")