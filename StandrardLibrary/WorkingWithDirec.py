from pathlib import Path

path = Path("PrimitveTypes")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename()
# we are iterating through the folder
for p in path.iterdir():
    print(p)
paths = [p for p in path.iterdir()]
print(paths)
# this will give us all the directories
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
