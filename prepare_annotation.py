import os
from glob import glob
from re import match

"""
fonction: List pairs of file name and its language and return the list
ex.
{'3-2': 'TRK', '1-1': 'JPN', '3-3': 'TRK', '3-1': 'TRK', '1-3': 'JPN', '1-2': 'JPN'}
"""
def listing_files():
    path = "/Users/ma/Library/Mobile Documents/com~apple~CloudDocs/tal/extraction/projet/src" # path to the corpus directory
    listing = {} # dict to put in pairs of file name & its language (CHS/ENG/FRA/JPN/KOR/TRK)
    for file in glob(os.path.join(path, "*.txt")):
        file_id = os.path.basename(file).split(".")[0] # pick up file name
        if match(r"1-*", file_id): # Japanese if name starts with "1-"
            listing[file_id] = "JPN"
        elif match(r"3-*", file_id):
            listing[file_id] = "TRK" # Turkish if name starts with "3-"
    return listing


"""
main fonction
"""

if __name__ == "__main__":
    print(listing_files())