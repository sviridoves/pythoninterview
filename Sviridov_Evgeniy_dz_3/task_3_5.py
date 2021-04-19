import os
import re


def make_file(file_name):
    if os.path.exists(file_name):
        print('Файл существует')
    else:
        tmp_text = [t for t in 'abcdefg']
        tmp_digit = [d for d in (1, 2, 3, 4, 5, 6, 7)]
        with open(file_name, 'w') as f:
            for t, d in zip(tmp_text, tmp_digit):
                if t in 'ce':
                    f.write(f'{t}{d}\n')
                    continue
                f.write(f'{t} {d}\n')
        open_and_read_file(os.path.abspath(file_name))


def open_and_read_file(full_path):
    with open(full_path, 'r+') as f:
        lines = f.read()
        r = re.findall(r'\w+\d+', lines)
        print('First:')
        print(r[0])
        print('All:')
        for item in r:
            print(item)

        r = re.finditer(r'\w+\d+', lines)
        new_value = 'new123'
        start = 0
        f.seek(start)
        for item in r:
            f.write(lines[start:item.span()[0]])
            f.write(new_value)
            start = item.span()[1]
        f.write(lines[start:])

        f.seek(0)
        new_lines = f.read()
        print('New file after replace:')
        print(new_lines)


make_file('task_3_5_test.txt')
