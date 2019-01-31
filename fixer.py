""" 
This script has following facilities:
- copy images that reside in the same markdown folder, to assets/images folder.
- change image paths in markdown files to global paths. (pointing to assets/images)
- renaming all png filenames and references to lowercases.
"""

import os

# POST_PATH = "_post/"
MARKDOWN_SUFFIX = ['.md','.markdown']

# get a list of all markdown files in _post directory
md_file_list = []
for (dirpath, dirnames, filenames) in os.walk('.'):
    for fname in filenames:
        for suffix in MARKDOWN_SUFFIX:
            if(len(fname.split(suffix)[-1])==0): # the suffix exists
                # append to file list
                md_file_list.append(os.path.join(dirpath,fname))

# deal with each md file
for fpath in md_file_list:
    with open(fpath,'a+') as f:
        f_text = f.read()
        # find all occurrences of image path patterns
        f_text.
        pass