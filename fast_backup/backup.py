# Requires python version 3.5 or higher
# Copies all new and updated source directory files to destination directory
# Exclude empty folders

import time
from sys import argv
from pathlib import Path
from shutil import copy

source_dir_count = 0
source_files_count = 0
copied_files_count = 0
updated_files_count = 0
data_size = 0

home_path = str(Path.home())
source_dir = argv[1]
dist_dir = argv[2]


def create_dir(p):
    try:
        p.mkdir(parents=True, exist_ok=True)
    except OSError:
        print('Creation of the directory %s failed, check path name and try again' % dist_path)


def check_path(p):
    if not p.exists():
        message = format('directory %s doesn\'t exist, would you like to create it? press y(yes), n(no)' % dist_dir)
        answer = input(message)
        if answer == 'y' or answer == 'Y':
            create_dir(p)
        elif answer == 'n' or answer == 'N':
            print('Destination directory doesn\'t exist')
            exit(0)
        else:
            check_path(p)


def copy_file(file, destination):
    global source_files_count
    global copied_files_count
    global updated_files_count
    global data_size
    source_files_count += 1

    dist_file_path = destination.joinpath(file.relative_to(source_path))

    if dist_file_path.exists():
        if dist_file_path.stat().st_mtime < file.stat().st_mtime:
            copy(file.absolute(), dist_file_path)
            updated_files_count += 1
            data_size += file.stat().st_size
    else:
        dist_dir = dist_file_path.parent
        create_dir(dist_dir)
        copy(file.absolute(), dist_dir)
        copied_files_count += 1
        data_size += file.stat().st_size


def copy_tree(source, destination):
    global source_dir_count

    if source.is_dir():
        source_dir_count += 1
        for path in source.iterdir():
            copy_tree(path, destination)
    else:
        copy_file(source, destination)


print()
print('Copy data from %s to %s' % (source_dir, dist_dir))
print()

source_path = Path(source_dir).expanduser()
if not source_path.exists():
    print('Source directory doesn\'t exist')
    exit(1)

dist_path = Path(dist_dir).expanduser()
check_path(dist_path)

start_time = int(round(time.time() * 1000))
copy_tree(source_path, dist_path)
finish_time = int(round(time.time() * 1000))

print('It has taken %d milliseconds ' % (finish_time - start_time))
print()
print('Total count of source packages:  %d' % source_dir_count)
print('Total count of source files:     %d' % source_files_count)
print('Total count of copied files:     %d' % copied_files_count)
print('Total count of updated files:    %d' % updated_files_count)
print()
print('Total copied data:               %d kB' % (data_size / 1024))
