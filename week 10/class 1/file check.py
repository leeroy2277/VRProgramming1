import os

dirname = "testDir"

def create_dir_if_no_existing(name):

    if not os.path.exists(name):
        os.mkdir(name)
        print("directory" + name + "created.")

    else:
        print("the supplied name is a directory that already exists.")

create_dir_if_no_existing("abc")

