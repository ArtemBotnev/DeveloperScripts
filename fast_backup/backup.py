from pathlib import Path
import time

source_dir_count = 0

source_files_count = 0
copied_files_count = 0

home_path = str(Path.home())
source_dir = '~/temp'
dist_dir = '~/test/directory'


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


def copy_file(file, destination):
    global source_files_count
    source_files_count += 1

    print(file.name.format())
    print(file.absolute())
    print(destination)

    print(file.relative_to(source_path))

    dist_file_path = destination.joinpath(file.relative_to(source_path))
    print(dist_file_path)
    if dist_file_path.exists():
        print(dist_file_path.stat().st_ctime)
    else:
        print(file.stat().st_mtime)


def copy_tree(source, destination):
    global source_dir_count

    if source.is_dir():
        source_dir_count += 1
        for path in source.iterdir():
            copy_tree(path, destination)
    else:
        copy_file(source, destination)


start_time = int(round(time.time() * 1000))

source_path = Path(source_dir).expanduser()
if not source_path.exists():
    print('Source directory doesn\'t exist')
    exit(1)

dist_path = Path(dist_dir).expanduser()
copy_tree(source_path, dist_path)

check_path(dist_path)

finish_time = int(round(time.time() * 1000))
print('It has taken %d milliseconds ' % (finish_time - start_time))
print('Total count of source packages: %d ' % source_dir_count)
print('Total count of source files: %d ' % source_files_count)
