import os

def walk(root_dir):
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(root_dir, topdown=False, followlinks=False):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            print(len(path) * '---', file)

def trav_dir(root):
    print(root)
    for i in os.listdir(root):
        fp = os.path.join(root, i)
        if os.path.isfile(fp):
            print(i)
        elif os.path.isdir(fp):
            trav_dir(fp)

if __name__ == '__main__':
    root = '/tmp/test'
    trav_dir(root)
