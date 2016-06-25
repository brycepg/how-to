import os
# Current directory
# If you call this from the current directory without abspath,
# then it will not work since __file__ is a relative path
os.path.dirname(os.path.abspath(__file__))

# Get all files in a directory
# Never use os.walk again
def all_sub_files(root):
    for path, subdirs, files in os.walk(root):
        for name in files:
            yield os.path.join(path, name)
