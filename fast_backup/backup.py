import os
from pathlib import Path
import time

home_path = str(Path.home())
source_dir = '~/temp'
dist_dir = '~/test/directory'


def create_path(d):
    if d[:2] == '~/':
        d = os.path.join(str(Path.home()), d[2:])
    else:
        d = os.path.join(str(Path.home()), d)

    return Path(d)


def create_dir(p):
    try:
        p.mkdir(parents=True, exist_ok=True)
    except OSError:
        print('Creation of the directory %s failed, check path name and try again' % dist_path)
    else:
        print('Successfully created the directory %s ' % dist_path)


def check_path(p):
    if not p.exists():
        message = format('directory %s doesn\'t, would you like to create it? press y(yes), n(no)' % dist_dir)
        answer = input(message)
        if answer == 'y':
            create_dir(p)
        elif answer == 'n':
            print('Destination directory doesn\'t exist')
            exit(0)
        else:
            check_path(p)


def copy_file(file):
    print(file.name.format())
    print(file.absolute())


def copy_tree(source):
    if source.is_dir():
        for path in source.iterdir():
            copy_tree(path)
    else:
        copy_file(source)


start_time = int(round(time.time() * 1000))

source_path = create_path(source_dir)
if not source_path.exists():
    print('Source directory doesn\'t exist')
    exit(1)

dist_path = create_path(dist_dir)
copy_tree(source_path)

check_path(dist_path)

finish_time = int(round(time.time() * 1000))
print('It has taken %d milliseconds ' % (finish_time - start_time))
