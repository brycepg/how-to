import os
# Current directory
# If you call this from the current directory without abspath,
# then it will not work since __file__ is a relative path
os.path.dirname(os.path.abspath(__file__))
