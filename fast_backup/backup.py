import os
from pathlib import Path

home_path = str(Path.home())
source_dir = '~/test/source'
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


# def copy_files():
#     source_path.ch


source_path = create_path(source_dir)
if not source_path.exists():
    print('Source directory doesn\'t exist')
    exit(1)

dist_path = create_path(dist_dir)

check_path(dist_path)
