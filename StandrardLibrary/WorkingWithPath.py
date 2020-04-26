from pathlib import Path

path = Path("Modules/sales.py")
# checks to see if the file is there
path.exists()
path.is_file()
path.is_dir()
# returns the file name
print(path.name)
# returns the name with out the extention
print(path.stem)
# returns the extention only
print(path.suffix)
# This return the parent folder or path
print(path.parent)
# this will change the suffix of sa file
path = path.with_suffix(".txt")
print(path.absolute())
