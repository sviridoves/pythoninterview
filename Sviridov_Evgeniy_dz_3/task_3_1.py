import os
from pathlib import Path


def get_file_name(file_name):
    full_path = os.path.abspath(file_name)
    if os.path.exists(full_path):
        result = Path(full_path).stem
    else:
        result = 'File not find'

    return result


if __name__ == '__main__':
    print(get_file_name('task_3_1.py'))
