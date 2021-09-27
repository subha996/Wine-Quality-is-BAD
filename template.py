# this py file is for creating standard template for the project,also can be used `coockicutter` libray


import os

# directory
dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True) # exist_ok=True means if the directory already exist, it will not raise error
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

# files
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass